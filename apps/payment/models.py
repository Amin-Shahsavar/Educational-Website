from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.discount.models import DiscountCode
from apps.plan.models import Plan


User = get_user_model()


class Purchase(models.Model):

    GATEWAY_TYPE = [
        ('PAYPAL', 'Paypal'),
        ('PARSIAN', 'Parsian'),
    ]

    PAYMENT_STATUS = [
        ('PAYING', 'Paying'),
        ('PAID', 'Paid'),
        ('CANCELED', 'Canceled'),
    ]

    user = models.ForeignKey(
        verbose_name=_('user'),
        to=User,
        on_delete=models.PROTECT,
    )
    plan = models.ForeignKey(
        verbose_name=_('plan'),
        to=Plan,
        on_delete=models.PROTECT,
    )
    discount_code = models.ForeignKey(
        verbose_name=_('discount code'),
        to=DiscountCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    gateway = models.CharField(_('gateway'), choices=GATEWAY_TYPE, default='PARSIAN')
    amount = models.PositiveIntegerField(_('amount'))
    card_number = models.CharField(_('card number'), max_length=16, blank=True, null=True)
    payment_number = models.CharField(_('payment number'), max_length=128)
    invoice_number = models.CharField(_('invoice number'), max_length=128)
    status = models.CharField(_('status'), choices=PAYMENT_STATUS, default='PAYING')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def is_expired(self):
        return self.status == 'PAYING' and self.created_at is not None and self.created_at < timezone.now() - timezone.timedelta(minutes=10)
    
    def expire_order(self):
        if self.status == 'PAYING':
            self.status = 'CANCELED'
            self.save()
