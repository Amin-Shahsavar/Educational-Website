from django.contrib import admin

from apps.setting.models import (
    Service,
    AppVersion,
    ContactUs,
)


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'title_en',
        'description',
        'description_en',
        'button_text',
        'button_link',
    ]


@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = [
        'release_date',
        'release_version',
        'is_deprecate',
    ]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'title',
        'description',
    ]
