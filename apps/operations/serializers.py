
from rest_framework import serializers

from apps.operations.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "license_number",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "full_name",
            "created_at",
            "updated_at",
        )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "license_number",
            "is_active",
        )


class DriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "license_number",
            "is_active",
        )