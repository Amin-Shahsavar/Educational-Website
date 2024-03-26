from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.notification.models import Notification
from apps.plan.models import Plan
from utils.validators.username_validator import UsernameValidator


class User(AbstractUser):

    REGION_CHOICES = [
        ('INSIDE', 'INSIDE'),
        ('OUTSIDE', 'OUTSIDE'),
    ]

    username_validator = UsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=128,
        unique=True,
        help_text=_("Required. 128 characters or fewer. Letters, digits and ./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        blank=True,
        null=True,
    )
    password = models.CharField(_('password'), max_length=128, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=128)
    last_name = models.CharField(_('last name'), max_length=128)
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text=_("Phone number with country code"),
    )
    email = models.EmailField(
        _('email'),
        max_length=265,
        unique=True,
        blank=True,
        null=True,
        help_text=_("Required for users outside of iran"),
        error_messages={
            "unique": _("کاربری با این ایمیل وجود دارد."),
        },
    )
    avatar = models.ImageField(
        _('avatar'),
        upload_to='./user/avatar/',
        blank=True,
        null=True,
    )
    is_verified = models.BooleanField(_('verify status'), default=False)
    region = models.CharField(_('region'), blank=True, null=True, choices=REGION_CHOICES)
    plan = models.ForeignKey(
        to=Plan,
        on_delete=models.SET_NULL,
        verbose_name=_('plan'),
        blank=True,
        null=True,
    )
    plan_purchase_date = models.DateTimeField(_('plan purchase date'), blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.username:
            self.username = self.username.lower()
        
        if not self.username:
            self.username = self.phone_number

        if self.email == '':
            self.email = None

        if (self.is_superuser or self.is_staff) and not self.password:
            raise ValidationError(
                _("پسورد اجباری است."),
            )

        if self.is_staff or self.is_superuser:
            self.is_verified = True

        if self.phone_number and self.phone_number.startswith('+98'):
            self.region = 'INSIDE'
        else:
            self.region = 'OUTSIDE'

        return super(User, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
