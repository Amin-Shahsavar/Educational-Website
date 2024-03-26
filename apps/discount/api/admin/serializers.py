from rest_framework import serializers

from apps.discount.models import DiscountCode


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = [
            'id',
            'title',
            'start_date',
            'end_date',
            'max_use',
            'toman_discount_amount',
            'dollar_discount_amount',
        ]
        extra_kwargs = {
            'title': {'required': True},
            'start_date': {'required': True},
            'end_date': {'required': True},
            'toman_discount_amount': {'required': True},
            'dollar_discount_amount': {'required': True},
        }
