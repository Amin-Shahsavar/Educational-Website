from django.contrib import admin

from apps.plan.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'title_en',
        'description',
        'description_en',
        'duration',
        'toman_price',
        'toman_price_discount',
        'dollar_price',
        'dollar_price_discount',
        'cover',
        'icon',
    ]
