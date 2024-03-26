from rest_framework import generics
from rest_framework.filters import SearchFilter

from utils.permissions.superuser import IsSuperUser
from utils.paginations.page_size import PageSizeNumberPagination
from apps.notification.api.admin.serializers import NotificationSerializer
from apps.notification.models import Notification


class ListCreateNotificationView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    search_fields = ['title', 'title_en']


class RetrieveUpdateDestroyNotificationView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
