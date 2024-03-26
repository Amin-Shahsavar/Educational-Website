from django.contrib.auth import get_user_model
from django.db.models import Sum

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.payment.models import Purchase

from utils.permissions.superuser import IsSuperUser


User = get_user_model()


class DashboardView(APIView):
    permission_classes = [IsSuperUser]

    @staticmethod
    def parsian_total_price():
        total_price = Purchase.objects.filter(gateway='PARSIAN', status='PAID').aggregate(Sum('amount'))['amount__sum']
        return total_price if total_price is not None else 0

    @staticmethod
    def paypal_total_price():
        total_price = Purchase.objects.filter(gateway='PAYPAL', status='PAID').aggregate(Sum('amount'))['amount__sum']
        return total_price if total_price is not None else 0

    def get(self, request, *args, **kwargs):
        dashboard = {
            'All_Users': User.objects.all().count(),
            'Inside_Users': User.objects.filter(region='INSIDE').count(),
            'Outside_Users': User.objects.filter(region='OUTSIDE').count(),
            'Purchases': Purchase.objects.filter(status='PAID').count(),
            'Inside_Purchases': Purchase.objects.filter(gateway='PARSIAN', status='PAID').count(),
            'Outside_Purchases': Purchase.objects.filter(gateway='PAYPAL', status='PAID').count(),
            'Total_Inside_Purchases': self.parsian_total_price(),
            'Total_Outside_Purchases': self.paypal_total_price(),
        }
        return Response(dashboard)
