from rest_framework import serializers

from apps.notification.models import Notification


class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'title',
            'title_en',
            'message',
            'message_en',
            'user_type',
        ]
