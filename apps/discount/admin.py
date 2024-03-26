from django.contrib import admin

from apps.discount.models import DiscountCode


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'start_date',
        'end_date',
        'max_use',
        'toman_discount_amount',
        'dollar_discount_amount',
    ]
