from django.contrib import admin

from apps.notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'title_en',
        'message',
        'message_en',
        'user_type',
    ]
    list_display = [
        'title',
        'title_en',
        'message',
        'message_en',
        'user_type',
    ]
