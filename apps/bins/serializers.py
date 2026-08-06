
from rest_framework import serializers

from apps.bins.models import (
    SmartBin,
    Alert,
)


# ============================================================================
# Smart Bin
# ============================================================================

class SmartBinSerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(
        source="zone.name",
        read_only=True,
    )

    facility_name = serializers.CharField(
        source="zone.facility.name",
        read_only=True,
    )

    organization_name = serializers.CharField(
        source="zone.facility.organization.name",
        read_only=True,
    )

    class Meta:
        model = SmartBin
        fields = (
            "id",
            "zone",
            "zone_name",
            "facility_name",
            "organization_name",
            "name",
            "code",
            "description",
            "capacity_liters",
            "fill_level",
            "battery_level",
            "status",
            "latitude",
            "longitude",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "zone_name",
            "facility_name",
            "organization_name",
            "created_at",
            "updated_at",
        )


class SmartBinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartBin
        fields = (
            "zone",
            "name",
            "code",
            "description",
            "capacity_liters",
            "fill_level",
            "battery_level",
            "status",
            "latitude",
            "longitude",
            "is_active",
        )


class SmartBinUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartBin
        fields = (
            "name",
            "description",
            "capacity_liters",
            "fill_level",
            "battery_level",
            "status",
            "latitude",
            "longitude",
            "is_active",
        )


# ============================================================================
# Alert
# ============================================================================

class AlertSerializer(serializers.ModelSerializer):
    smart_bin_name = serializers.CharField(
        source="smart_bin.name",
        read_only=True,
    )

    zone_name = serializers.CharField(
        source="smart_bin.zone.name",
        read_only=True,
    )

    class Meta:
        model = Alert
        fields = (
            "id",
            "smart_bin",
            "smart_bin_name",
            "zone_name",
            "alert_type",
            "title",
            "message",
            "severity",
            "status",
            "triggered_at",
            "resolved_at",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "smart_bin_name",
            "zone_name",
            "triggered_at",
            "created_at",
            "updated_at",
        )


class AlertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = (
            "smart_bin",
            "alert_type",
            "title",
            "message",
            "severity",
            "status",
        )


class AlertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = (
            "title",
            "message",
            "severity",
            "status",
            "resolved_at",
        )