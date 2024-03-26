from django.db import models
from django.utils.translation import gettext_lazy as _


class DiscountCode(models.Model):
    title = models.CharField(_('title'), max_length=128, unique=True)
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    max_use = models.PositiveIntegerField(_('max use'), blank=True, null=True)
    toman_discount_amount = models.PositiveIntegerField(_('toman discount amount'))
    dollar_discount_amount = models.DecimalField(_('dollar discount amount'), max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.title
