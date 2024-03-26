from rest_framework import serializers

from apps.payment.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    phone_number = serializers.ReadOnlyField(source='user.phone_number')
    email = serializers.ReadOnlyField(source='user.email')
    plan = serializers.ReadOnlyField(source='plan.title')
    discount_code = serializers.ReadOnlyField(source='discount_code.title')
    class Meta:
        model = Purchase
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
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
        read_only_fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'plan',
            'discount_code',
            'gateway',
            'amount',
            'cart_number',
            'payment_number',
            'status',
            'created_at',
            'updated_at',
        ]
        