from django.db import models
from django.utils.translation import gettext_lazy as _


class Plan(models.Model):
    title = models.CharField(_('title'), max_length=256, unique=True)
    title_en = models.CharField(_('title (EN)'), max_length=256, unique=True)
    description = models.TextField(_('description'))
    description_en = models.TextField(_('descriptin (EN)'))
    duration = models.PositiveIntegerField(_('duration'), default=365)
    toman_price = models.PositiveIntegerField(_('toman price'))
    toman_price_discount = models.PositiveIntegerField(_('toman price discount'))
    dollar_price = models.DecimalField(_('dollar price'), max_digits=8, decimal_places=2)
    dollar_price_discount = models.DecimalField(_('dollar price discount'), max_digits=8, decimal_places=2)
    cover = models.ImageField(
        _('cover'),
        upload_to='./plans/covers',
        blank=True,
        null=True,
    )
    icon = models.ImageField(
        _('icon'),
        upload_to='./plans/icons',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
