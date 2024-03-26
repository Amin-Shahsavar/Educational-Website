from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.course.models import (
    Course,
    Video,
    Image,
    Pdf,
    Category,
)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PdfInline(admin.TabularInline):
    model = Pdf
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Course info'),
            {
                'fields': (
                    'title',
                    'title_en',
                    'description',
                    'description_en',
                    'cover',
                    'icon',
                    'region',
                ),
            },
        ),
        (_('Plan'),
            {
                'fields': ('plan',)
            },
        ),
        (_('Category'),
            {
                'fields': ('category',)
            },
        ),
    )
    inlines = [VideoInline, ImageInline, PdfInline]
    list_display = ['title', 'region', 'plan', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_en', 'parent_category']
    fields = ['title', 'title_en', 'description', 'description_en', 'cover', 'icon', 'parent_category']
