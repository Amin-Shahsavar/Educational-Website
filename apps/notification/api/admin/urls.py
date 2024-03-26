from django.urls import path

from apps.notification.api.admin import views


Notifications = [
    path(
        'notification/',
        views.ListCreateNotificationView.as_view(),
        name='Notification List Create',
    ),
    path(
        'notification/<int:pk>/',
        views.RetrieveUpdateDestroyNotificationView.as_view(),
        name='Notification Retrieve Update Destroy',
    ),
]

urlpatterns = Notifications
