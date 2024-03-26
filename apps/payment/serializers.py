from rest_framework import serializers

from apps.payment.models import Purchase
from apps.plan.models import Plan


# class PurchaseSerializer(serializers.ModelSerializer):
#     first_name = serializers.ReadOnlyField(source='user.first_name')
#     last_name = serializers.ReadOnlyField(source='user.last_name')
#     phone_number = serializers.ReadOnlyField(source='user.phone_number')
#     email = serializers.ReadOnlyField(source='user.email')
#     # plan = serializers.ReadOnlyField(source='plan.title')
#     amount = serializers.IntegerField(read_only=True, source='plan.dollar_price_discount')
#     discount_code = serializers.ReadOnlyField(source='discount_code.title')
#     gateway = serializers.ReadOnlyField(source='gateway.title')

#     def get_amount(self, obj):
#         plan_instance = obj.dollar_price_discount.get('plan')
#         amount = plan_instance.amount
#         return amount

#     class Meta:
#         model = Purchase
#         fields = [
#             'id',
#             'first_name',
#             'last_name',
#             'phone_number',
#             'email',
#             'plan',
#             'discount_code',
#             'gateway',
#             'amount',
#             'card_number',
#             'payment_number',
#             'status',
#             'created_at',
#             'updated_at',
#         ]
#         read_only_fields = [
#             'id',
#             'first_name',
#             'last_name',
#             'phone_number',
#             'email',
#             'gateway',
#             'amount',
#             'card_number',
#             'payment_number',
#             'status',
#             'created_at',
#             'updated_at',
#         ]
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

        extra_kwargs = {
            'user': {'read_only': True},
            'gateway': {'read_only': True},
            'amount': {'read_only': True},
            'card_number': {'read_only': True},
            'payment_number': {'read_only': True},
            'invoice_number': {'read_only': True},
            'status': {'read_only': True},
        }
