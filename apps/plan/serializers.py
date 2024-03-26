from rest_framework import serializers

from apps.plan.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'id',
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
