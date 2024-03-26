from collections.abc import Iterable
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):

    USER_TYPE = (
        ('ALL', 'All Users'),
        ('FREE', 'Users Without Plan'),
        ('VIP', 'Users Whith Plan'),
        ('INSIDE', 'Users Inside Iran'),
        ('OUTSIDE', 'Users Outside Iran'),
    )

    title = models.CharField(_('title'), max_length=128)
    title_en = models.CharField(_('title (EN)'), max_length=128)
    message = models.TextField(_('message'))
    message_en = models.TextField(_('message (EN)'))
    user_type = models.CharField(_('send for'), choices=USER_TYPE, default='ALL')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self) -> str:
        return self.title
