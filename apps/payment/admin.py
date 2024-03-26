from django.contrib import admin

from apps.payment.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    fields = [
        'user',
        'plan',
        'discount_code',
        'gateway',
        'amount',
        'card_number',
        'payment_number',
        'status',
    ]
    list_display = [
        'user',
        'plan',
        'discount_code',
        'gateway',
        'amount',
        'card_number',
        'payment_number',
        'status',
        'created_at',
        'updated_at',
    ]
