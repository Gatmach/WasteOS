
from rest_framework import serializers

from apps.organizations.models import (
    Organization,
    Facility,
    Zone,
)


# ============================================================================
# Organization
# ============================================================================

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "code",
            "email",
            "phone",
            "address",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "name",
            "code",
            "email",
            "phone",
            "address",
            "is_active",
        )


class OrganizationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "name",
            "email",
            "phone",
            "address",
            "is_active",
        )


# ============================================================================
# Facility
# ============================================================================

class FacilitySerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True,
    )

    class Meta:
        model = Facility
        fields = (
            "id",
            "organization",
            "organization_name",
            "name",
            "code",
            "facility_type",
            "address",
            "latitude",
            "longitude",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "organization_name",
            "created_at",
            "updated_at",
        )


class FacilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = (
            "organization",
            "name",
            "code",
            "facility_type",
            "address",
            "latitude",
            "longitude",
            "is_active",
        )


class FacilityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = (
            "name",
            "facility_type",
            "address",
            "latitude",
            "longitude",
            "is_active",
        )


# ============================================================================
# Zone
# ============================================================================

class ZoneSerializer(serializers.ModelSerializer):
    facility_name = serializers.CharField(
        source="facility.name",
        read_only=True,
    )

    class Meta:
        model = Zone
        fields = (
            "id",
            "facility",
            "facility_name",
            "name",
            "code",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "facility_name",
            "created_at",
            "updated_at",
        )


class ZoneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = (
            "facility",
            "name",
            "code",
            "description",
            "is_active",
        )


class ZoneUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = (
            "name",
            "description",
            "is_active",
        )