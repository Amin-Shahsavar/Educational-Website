from rest_framework import serializers

from apps.setting.models import Service, AppVersion, ContactUs


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'title',
            'title_en',
            'description',
            'description_en',
            'button_text',
            'button_link',
        ]


class AppVersionSerializer(serializers.ModelSerializer):
    app_version = serializers.CharField(write_only=True)
    class Meta:
        model = AppVersion
        fields = [
            'id',
            'release_date',
            'release_version',
            'is_deprecate',
            'app_version',
        ]
        read_only_fields = [
            'release_date',
            'release_version',
            'is_deprecate',
        ]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'title',
            'description',
        ]
