from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(_('title'), max_length=128)
    title_en = models.CharField(_('title (EN)'), max_length=128)
    description = models.TextField(_('description'))
    description_en = models.TextField(_('description (EN)'))
    button_text = models.CharField(_('button text'), max_length=128)
    button_link = models.CharField(_('button url'), max_length=256)

    def __str__(self) -> str:
        return self.title


class AppVersion(models.Model):
    release_date = models.DateTimeField(_('release date'), auto_now_add=True)
    release_version = models.CharField(_('release version'), max_length=64, unique=True)
    is_deprecate = models.BooleanField(_(' is deprecate'), default=False)

    def __str__(self) -> str:
        return self.release_version


class ContactUs(models.Model):
    first_name = models.CharField(_('first name'), max_length=128)
    last_name = models.CharField(_('last name'), max_length=128)
    phone_number = models.CharField(_('phone number'), max_length=128, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    title = models.CharField(_('title'), max_length=128, blank=True, null=True)
    description = models.TextField(_('description'))

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
