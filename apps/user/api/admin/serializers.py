from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class SuperUserSerializer(serializers.ModelSerializer):
    password_conf = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'password_conf',
            'email',
        ]
        extra_kwargs = {
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {
                'required': True,
                'write_only': True,
            },
            'email': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_staff': {'read_only': True},
        }


class LoginSuperUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'region', 'plan']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'region', 'plan']
        read_only_fields = ['first_name', 'last_name', 'phone_number', 'email', 'region']
