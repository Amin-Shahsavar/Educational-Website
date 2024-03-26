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
        extra_kwargs = {
            'title': {'required': True},
            'title_en': {'required': True},
            'description': {'required': True},
            'description_en': {'required': True},
            'duration': {'required': True},
        }
