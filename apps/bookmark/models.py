from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.course.models import Course


User = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name=_('course'),
    )

    class Meta:
        unique_together = ('user', 'course')
