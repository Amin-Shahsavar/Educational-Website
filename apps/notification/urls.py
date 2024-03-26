from django.urls import path

from apps.notification import views


UserNotifications = [
    path(
        'notification/',
        views.ListUserNotificationView.as_view(),
        name='User Notification List',
    ),
    path(
        'notification/<int:pk>/',
        views.RetrieveUserNotificationView.as_view(),
        name='User Notification Retrieve',
    ),
]

urlpatterns = UserNotifications
