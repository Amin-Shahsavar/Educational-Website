from django.urls import path

from apps.discount.api.admin import views


DiscountCodes = [
    path(
        'discount/',
        views.ListCreateDiscountCodeView.as_view(),
        name='DiscountCode List Create'
    ),
    path(
        'discount/<int:pk>/',
        views.RetrieveUpdateDestroyDiscountCodeView.as_view(),
        name='DiscountCode Retrieve Update Destroy'
    ),
]

urlpatterns = DiscountCodes
