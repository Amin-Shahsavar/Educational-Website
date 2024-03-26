from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.plan.models import Plan


class Category(models.Model):
    title = models.CharField(_('title'), max_length=128)
    title_en = models.CharField(_('title (EN)'), max_length=128)
    description = models.TextField(_('description'), blank=True, null=True)
    description_en = models.TextField(_('description (EN)'), blank=True, null=True)
    cover = models.ImageField(
        _('cover'),
        upload_to='./categories/covers',
        blank=True,
        null=True,
    )
    icon = models.ImageField(
        _('icon'),
        upload_to='./categories/icons',
        blank=True,
        null=True,
    )
    parent_category = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name=_('parent category'),
        related_name='childrens',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
    
    def get_full_path(self):
        if self.sub_category:
            return f'{self.sub_category.get_full_path()} > {self.title}'
        return self.title
    
    def save(self, *args, **kwargs):
        if self.description == '':
            self.description = None
        if self.description_en == '':
            self.description_en = None
        return super().save(*args, **kwargs)


class Course(models.Model):

    REGION_CHOICES = [
        ('ALL', 'ALL'),
        ('INSIDE', 'INSIDE'),
        ('OUTSIDE', 'OUTSIDE'),
    ]

    title = models.CharField(_('title'), max_length=256)
    title_en = models.CharField(_('title (EN)'), max_length=256)
    description = models.TextField(_('description'), blank=True, null=True)
    description_en = models.TextField(_('description (EN)'), blank=True, null=True)
    cover = models.ImageField(
        _('cover'),
        upload_to='./courses/covers',
        blank=True,
        null=True,
    )
    icon = models.ImageField(
        _('icon'),
        upload_to='./courses/icons',
        blank=True,
        null=True,
    )
    region = models.CharField(_('region'), choices=REGION_CHOICES)
    plan = models.ForeignKey(
        to=Plan,
        verbose_name=_('plans'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name=_('category'),
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class Video(models.Model):

    REGION_CHOICES = [
        ('INSIDE', 'INSIDE'),
        ('OUTSIDE', 'OUTSIDE'),
    ]

    title = models.CharField(_('title'), max_length=256, blank=True, null=True)
    title_en = models.CharField(_('title (EN)'), max_length=256, blank=True, null=True)
    video = models.FileField(_('video'), upload_to='./courses/videos')
    region = models.CharField(_('region'), choices=REGION_CHOICES)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name=_('for course'),
        related_name='videos',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class Image(models.Model):

    REGION_CHOICES = [
        ('INSIDE', 'INSIDE'),
        ('OUTSIDE', 'OUTSIDE'),
    ]

    title = models.CharField(_('title'), max_length=256, blank=True, null=True)
    title_en = models.CharField(_('title (EN)'), max_length=256, blank=True, null=True)
    image = models.FileField(_('video'), upload_to='./courses/images')
    region = models.CharField(_('region'), choices=REGION_CHOICES)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name=_('for course'),
        related_name='images',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class Pdf(models.Model):

    REGION_CHOICES = [
        ('INSIDE', 'INSIDE'),
        ('OUTSIDE', 'OUTSIDE'),
    ]

    title = models.CharField(_('title'), max_length=256, blank=True, null=True)
    title_en = models.CharField(_('title (EN)'), max_length=256, blank=True, null=True)
    pdf = models.FileField(_('video'), upload_to='./courses/Pdfs')
    region = models.CharField(_('region'), choices=REGION_CHOICES)
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name=_('for course'),
        related_name='pdfs',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title
