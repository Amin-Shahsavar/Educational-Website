from django.urls import path

from apps.user import views


Users = [
    path(
        'register/',
        views.UserRegistrationView.as_view(),
        name='User Registration',
    ),
    path(
        'login/',
        views.UserLoginSendMessageView.as_view(),
        name='User Login',
    ),
    path(
        'profile/',
        views.UserProfileView.as_view(),
        name='User Profile',
    ),
    path(
        'profile/change-avatar/',
        views.ChangeAvatarView.as_view(),
        name='User Change Avatar',
    ),
    path(
        'profile/change-profile/',
        views.ChangeProfileView.as_view(),
        name='User Change Profile',
    )
]

urlpatterns = Users
