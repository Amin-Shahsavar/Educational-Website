from django.urls import path

from apps.payment.api.admin import views


Payments = [
    path(
        'purchase/',
        views.ListPurchaseView.as_view(),
        name='Purchase List',
    ),
    path(
        'purchase/<int:pk>/',
        views.RetrievePurchaseView.as_view(),
        name='Purchase Retrieve',
    ),
]

urlpatterns = Payments
