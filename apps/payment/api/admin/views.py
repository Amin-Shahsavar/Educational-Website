from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.payment.api.admin.serializers import PurchaseSerializer
from apps.payment.models import Purchase
from utils.paginations.page_size import PageSizeNumberPagination
from utils.permissions.superuser import IsSuperUser


class ListPurchaseView(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    search_fields = [
        'user__first_name',
        'user__last_name',
        'user__phone_number',
        'plan__title',
        'payment_number',
    ]


class RetrievePurchaseView(generics.RetrieveAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
