from django.urls import path

from apps.payment import views


Payments = [
    # path('create_order/', views.CreateOrder.as_view(), name='create_order'),
    # path('order_detail/<str:order_id>/', views.OrderDetail.as_view(), name='order_detail'),
    # path('return_order/' , views.ReturnOrder.as_view() , name='return_order'),
    # path('cancel_order/' , views.CancelOrder.as_view() , name='cancel_order'),
    # path('show-payments/' , views.ShowPayments.as_view() , name='show-payments' ),
    path('pay/', views.PaymentView.as_view(), name='payment'),
]

urlpatterns = Payments
