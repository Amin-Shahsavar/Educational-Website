from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None,
            {
                'fields': ('username', 'password'),
            },
        ),
        (_('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'avatar',
                    'region',
                    'is_verified',
                ),
            },
        ),
        (_('Plan status'),
            {
                'fields': (
                    'plan',
                ),
            },
        ),
        (_('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important datas'),
            {
                'fields': ('last_login', 'date_joined'),
            },
        ),
    )
    add_fieldsets = (
        (None,
            {
                'fields': (
                    'username',
                    'password1',
                    'password2',
                    'phone_number',
                    'email',
                    'first_name',
                    'last_name',
                ),
            },
        ),
    )
