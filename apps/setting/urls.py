from django.urls import path

from apps.setting import views


Services = [
    path(
        'service/',
        views.ListServiceView.as_view(),
        name='Servise List',
    ),
    path(
        'service/<int:pk>/',
        views.RetrieveServiceView.as_view(),
        name='Service Retrieve',
    ),
]

AppVersion = [
    path(
        'appversion/',
        views.CheckAppVersionView.as_view(),
        name='App Version Check',
    ),
]

ContactUs = [
    path(
        'contactus/',
        views.CreateContactUsView.as_view(),
        name='Contact Us Create',
    ),
]

urlpatterns = Services + AppVersion + ContactUs
