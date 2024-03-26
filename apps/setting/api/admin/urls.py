from django.urls import path

from apps.setting.api.admin import views


Services = [
    path(
        'service/',
        views.ListCreateServiceView.as_view(),
        name='Service List Create',
    ),
    path(
        'service/<int:pk>/',
        views.RetrieveUpdateDestroyServiceView.as_view(),
        name='Service Retrieve Update Destroy',
    ),
]

AppVersion = [
    path(
        'appversion/',
        views.ListCreateAppVersionView.as_view(),
        name='App Version List Create',
    ),
    path(
        'appversion/<int:pk>/',
        views.RetrieveUpdateDestrotyAppVersionView.as_view(),
        name='App Version Retrieve Update Destroy',
    ),
]

ContactUs = [
    path(
        'contactus/',
        views.ListContactUsView.as_view(),
        name='Contact Us List',
    ),
    path(
        'contactus/<int:pk>/',
        views.RetrieveContactUsView.as_view(),
        name='Contact Us Retrieve',
    ),
]

urlpatterns = Services + AppVersion + ContactUs
