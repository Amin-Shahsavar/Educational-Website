from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import requests
import datetime
from decouple import config
import json
from xml.etree import ElementTree as ET

from apps.discount.models import DiscountCode
from apps.payment.models import Purchase
from apps.payment.serializers import PurchaseSerializer
from apps.payment.tasks import expire_payments
from apps.plan.models import Plan
from utils.payment.paypal_access_token import calculate_remaining_time, get_paypal_accsess_token


class PaymentView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    def get_amount(self, request, plan, *args, **kwargs) -> int:
        plan = Plan.objects.get(id=plan)
        discount_code = request.data.get('discount_code', '')
        
        if request.user.region == 'INSIDE':
            if discount_code:
                discount = DiscountCode.objects.get(id=discount_code)
                amount = plan.toman_price_discount - discount.toman_discount_amount
            else:
                amount = plan.toman_price_discount

            if amount < 1000:
                return Response(
                    {'amount': 'The amount must be more than 1000'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            amount = plan.dollar_price_discount
        print('Amount:', amount)
        return amount

    def post(self, request, *args, **kwargs):
        LoginAccount = 'ge6od631p2lE1t2181qt'
        OrderId = 34567
        Amount = self.get_amount(request=request, plan=request.data.get('plan'))
        CallBackUrl = 'http://127.0.0.1:8000/payment/verify/'
        Originator = '989300968349'

        url = 'https://pec.shaparak.ir/NewIPGServices/Sale/SaleService.asmx'
        soap_action = 'https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService/SalePaymentRequest'

        data = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
          <soap12:Body>
            <SalePaymentRequest xmlns="https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService">
                <requestData>
                    <LoginAccount>{LoginAccount}</LoginAccount>
                    <OrderId>{OrderId}</OrderId>
                    <Amount>{Amount}</Amount>
                    <CallBackUrl>{CallBackUrl}</CallBackUrl>
                    <Originator>{Originator}</Originator>
                </requestData>
            </SalePaymentRequest>
          </soap12:Body>
        </soap12:Envelope>"""

        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': soap_action,
        }

        response = requests.post(url=url, data=data, headers=headers)
        print('Response Status:', response)
        print("Response:", response.text)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            ns = {'ns': 'https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService'}
            token_element = root.find('.//ns:Token', namespaces=ns)
            if token_element is not None:
                if not token_element.text == 0:
                    token = token_element.text
                    print('Token:', token)
                    Purchase.objects.create(
                        user=request.user,
                        plan=Plan.objects.get(id=request.data.get('plan')),
                        # discount_code=DiscountCode.objects.get(id=request.data.get('discount_code')),
                        gateway='PARSIAN',
                        amount=Amount,
                        payment_number=1234,
                        invoice_number=1234,
                        status='PAYING',
                    )
                    return Response(
                        {'Payment Url': f"https://pec.shaparak.ir/NewIPG/?token={token}"},
                        status=status.HTTP_200_OK,
                    )
            else:
                return Response(
                    {'error': 'Token not found in the response'},
                    status=status.HTTP_404_NOT_FOUND,
                )
        print('Response:', response)
        return Response(response)


# base_url = config('PAYPAL_BASE_URL')


# class CreateOrder(APIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#     permission_classes = [IsAuthenticated]

#     def get_amount(self, plan, user):

#         if user.region == 'INSIDE':
#             amount = plan.toman_price_discount
#         else:
#             amount = plan.dollar_price_discount
#         print('in chieeeeeeeeeeeeeeeeeeeeeeeeeeeee', amount)

#         return amount

#     def post(self, request):
#         current_site = get_current_site(request)

#         # validate order details from the request
#         serializer = self.serializer_class(
#             data=request.data, context={'request': request})
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as e:
#             return Response({'status': f'{e}'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#         existing_order = None
#         try:
#             existing_order = Purchase.objects.filter(
#                 user=request.user, status='Created').first()
#             order_id = existing_order.payment_number
#         except:
#             order_id = None
#         approve_link = config('PAYPAL_APPROVE_LINK')
#         if existing_order:
#             if existing_order.is_expired():
#                 existing_order.expire_order()
#                 return Response(
#                     {'status': 'Your order has expired and has been canceled.'},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             else:
#                 return Response({'status': f'you have already opened order you can countinue with this link : {approve_link}{order_id}',
#                                  'cancel_order': f'you can cancel this order now to click this link : {current_site}{reverse("cancel_order")}?token={order_id}',
#                                  }, status=status.HTTP_200_OK)
#         if request.user.plan:
#             return Response({'status': 'User already has a plan'}, status=status.HTTP_400_BAD_REQUEST)
#         plan = serializer.validated_data['plan']
#         order_data = {
#             "intent": "CAPTURE",
#             "purchase_units": [
#                 {
#                     "amount": {
#                         "currency_code": "USD",
#                         "value": self.get_amount(plan, request.user),
#                     }
#                 }
#             ],
#             "application_context": {
#                 "cancel_url": f"{current_site}{reverse('cancel_order')}",
#                 "return_url": f"{current_site}{reverse('return_order')}",
#                 "user_action": "PAY_NOW",

#             }
#         }
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {get_paypal_accsess_token()}"
#         }
#         print('this is header  ::: ',headers)
#         print(order_data)

#         # try:
#         # Send the request to create the order
#         response = requests.post(
#             f"{base_url}checkout/orders",
#             json=order_data,
#             headers=headers
#         )
#         print(response.status_code)
#         print(response.text)
#         response.raise_for_status()
#         data = response.json()

#         if response.status_code == 201:
#             order_id = data['id']
#             # Create or update the order in your database
#             order_instance, created = Purchase.objects.get_or_create(
#                 payment_number=order_id,
#                 defaults={
#                     'user': request.user,
#                     'payment_number': order_id,
#                     'plan': plan,
#                     'amount': self.get_amount(plan, request.user),
#                 }
#             )
#             order_instance.save()
#             approve_link = next(
#                 link for link in data['links'] if link['rel'] == 'approve')
#             expire_payments.apply_async(
#                 args=(order_id,), eta=timezone.now() + timezone.timedelta(minutes=10))
#             return Response({'status': 'Order Created Successfully', 'approve link': f'{approve_link["href"]}', 'order_id': f'{order_id}'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'status': 'Failed to create order'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         # except Exception as e:
#         #     return Response({'status': f'{e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class OrderDetail(APIView):

#     def get(self, request, order_id):
#         try:
#             order = Purchase.objects.get(order_id=order_id)
#         except Purchase.DoesNotExist:
#             return Response({'mesaage': 'orderid not found !'}, status=status.HTTP_404_NOT_FOUND)
#         headers = {
#             "Authorization": f"Bearer {get_paypal_accsess_token()}"
#         }

#         detail = requests.get(
#             f'{base_url}checkout/orders/{order_id}', headers=headers)
#         response_data = detail.json()
#         if 'status' in response_data:
#             if order.is_expired():
#                 response_data['remaining_time'] = 'Expired'
#             elif order.status == 'Expired':
#                 response_data['remaining_time'] = 'Expired'
#             elif order.status == 'Cancelled':
#                 response_data['remaining_time'] = 'Canceled'
#             else:
#                 remaining_time = calculate_remaining_time(order.created_at)
#                 response_data['remaining_time'] = str(remaining_time)
#         return Response(response_data)


# class ReturnOrder(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         order_id = request.GET.get('token')
#         payer_id = request.GET.get('PayerID')
#         order_detail = OrderDetail()
#         response_data = order_detail.get(
#             request=request, order_id=order_id).data
#         paypal_status = response_data['status']
#         payer = response_data['payer']
#         paypal_payer_id = response_data['payer']['payer_id']
#         if payer_id == paypal_payer_id:
#             try:
#                 order = Purchase.objects.get(
#                     order_id=order_id, status='Created')
#                 headers = {
#                     "Content-Type": "application/json",
#                     "Authorization": f"Bearer {get_paypal_accsess_token()}"
#                 }
#                 response = requests.post(
#                     f'{base_url}checkout/orders/{order_id}/capture', headers=headers)
#                 if response.status_code == 201:
#                     order.is_ordered = True
#                     order.status = 'Completed'
#                     order.save()
#                     Purchase.objects.create(
#                         user=order.user,
#                         order=order,
#                         transaction_id=order.order_id,
#                         amount=order.amount,
#                         payer=payer,
#                         plan=order.plan
#                     )
#                     # enable user plan
#                     user = order.user
#                     User.objects.filter(id=user.id).update(
#                         has_plan=True,
#                         plan=order.plan,
#                         plan_started_at=datetime.date.today(),
#                         plan_end_at=datetime.date.today() +
#                         datetime.timedelta(days=order.plan.duration),
#                     )

#                     return Response({'status': 'OrderComplated'}, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'status': 'Faild ! Order Not Compalted.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#             except Exception as e:
#                 return Response({'Status': 'Order id Not Found or Expired!', 'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({'status': 'Complate Order Faild ! Payer Id not Match !'}, status=status.HTTP_400_BAD_REQUEST)


# class CancelOrder(APIView):

#     def get(self, request):
#         order_id = request.GET.get('token')
#         try:
#             order = Purchase.objects.get(order_id=order_id)
#             if not order.status == "Completed":
#                 order.status = 'Cancelled'
#                 order.save()
#             else:
#                 return Response({'status': 'this order is complated !! '}, status=status.HTTP_400_BAD_REQUEST)
#             return Response({'status': 'Order Canceled'}, status=status.HTTP_204_NO_CONTENT)

#         except:
#             return Response({'status': 'order not found or deleted'}, status=status.HTTP_404_NOT_FOUND)


# class ShowPayments(generics.ListAPIView):
#     serializer_class = PurchaseSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Purchase.objects.filter(user=user)