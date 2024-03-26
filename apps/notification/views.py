from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.notification.models import Notification
from apps.notification.serializers import UserNotificationSerializer
from utils.paginations.page_size import PageSizeNumberPagination


User = get_user_model()


class ListUserNotificationView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageSizeNumberPagination
    serializer_class = UserNotificationSerializer

    def get_queryset(self):
        user = self.request.user

        if user.region == 'INSIDE' and user.plan == None:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'INSIDE', 'FREE'])

        elif user.region == 'INSIDE' and user.plan:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'INSIDE', 'VIP'])

        elif user.region == 'OUTSIDE' and user.plan == None:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'OUTSIDE', 'FREE'])

        elif user.region == 'OUTSIDE' and user.plan:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'OUTSIDE', 'VIP'])

        else:
            queryset = Notification.objects.filter(user_type='ALL')

        return queryset


class RetrieveUserNotificationView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserNotificationSerializer

    def get_queryset(self):
        user = self.request.user

        if user.region == 'INSIDE' and user.plan == None:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'INSIDE', 'FREE'])

        elif user.region == 'INSIDE' and user.plan:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'INSIDE', 'VIP'])

        elif user.region == 'OUTSIDE' and user.plan == None:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'OUTSIDE', 'FREE'])

        elif user.region == 'OUTSIDE' and user.plan:
            queryset = Notification.objects.filter(user_type__in=['ALL', 'OUTSIDE', 'VIP'])

        else:
            queryset = Notification.objects.filter(user_type='ALL')

        return queryset
