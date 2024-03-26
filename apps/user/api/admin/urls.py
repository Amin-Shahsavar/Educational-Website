from django.urls import path

from apps.user.api.admin import views


Users = [
    path(
        'user/',
        views.ListUserView.as_view(),
        name='Users List',
    ),
    path(
        'user/<int:pk>/',
        views.RetrieveUpdateUserView.as_view(),
        name='User Retrieve Update',
    ),
]

SuperUsers = [
    path(
        'superuser/',
        views.ListCreateSuperUserView.as_view(),
        name='SuperUsers List Create',
    ),
    path(
        'superuser/<int:pk>/',
        views.RetrieveDestroySuperUserView.as_view(),
        name='SuperUser Retrieve Destroy',
    ),
    path(
        'loginsuperuser/',
        views.LoginSuperUserView.as_view(),
        name='SuperUsers Login',
    ),
]

urlpatterns = Users + SuperUsers
