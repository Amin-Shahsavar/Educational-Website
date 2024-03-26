from rest_framework import generics
from rest_framework.filters import SearchFilter

from utils.permissions.superuser import IsSuperUser
from utils.paginations.page_size import PageSizeNumberPagination
from apps.setting.api.admin.serializers import (
    ServiceSerializer,
    AppVersionSerializer,
    ContactUsSerializer,
)
from apps.setting.models import (
    Service,
    AppVersion,
    ContactUs,
)


class ListCreateServiceView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    search_fields = ['title', 'title_en']


class RetrieveUpdateDestroyServiceView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ListCreateAppVersionView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = AppVersionSerializer
    queryset = AppVersion.objects.all()
    search_fields = ['release_date', 'release_version', 'is_deprecate']


class RetrieveUpdateDestrotyAppVersionView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = AppVersionSerializer
    queryset = AppVersion.objects.all()


class ListContactUsView(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()
    search_fields = ['first_name', 'last_name', 'phone_number', 'email', 'title']


class RetrieveContactUsView(generics.RetrieveAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()
