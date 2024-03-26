from django.utils import timezone

from apps.payment.models import Purchase

from celery import shared_task


@shared_task
def expire_payments(payment_number):
    try:
        purchase = Purchase.objects.get(payment_number=payment_number)
        if purchase.status == 'PAYING' and purchase.created_at < timezone.now() - timezone.timedelta(minutes=10):
            purchase.expire_order()
    except Purchase.DoesNotExist:
        pass
