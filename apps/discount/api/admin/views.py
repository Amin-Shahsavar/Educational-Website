from rest_framework import generics
from rest_framework.filters import SearchFilter

from apps.discount.api.admin.serializers import DiscountCodeSerializer
from apps.discount.models import DiscountCode
from utils.paginations.page_size import PageSizeNumberPagination
from utils.permissions.superuser import IsSuperUser


class ListCreateDiscountCodeView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()
    search_fields = ['title']


class RetrieveUpdateDestroyDiscountCodeView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()
