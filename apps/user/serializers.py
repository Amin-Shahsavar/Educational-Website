from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'avatar',
            'region',
        ]
        extra_kwargs = {
            'region': {'read_only': True},
            'avatar': {'read_only': True},
        }


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'email']
        extra_kwargs = {
            'phone_number': {'required': True},
            'email': {'required': False},
        }


class ChangeAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']


class ChangeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
