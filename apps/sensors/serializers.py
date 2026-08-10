
from rest_framework import serializers

from apps.sensors.models import (
    Sensor,
    SensorReading,
)


# ============================================================================
# Sensor
# ============================================================================

class SensorSerializer(serializers.ModelSerializer):
    smart_bin_name = serializers.CharField(
        source="smart_bin.name",
        read_only=True,
    )

    zone_name = serializers.CharField(
        source="smart_bin.zone.name",
        read_only=True,
    )

    class Meta:
        model = Sensor
        fields = (
            "id",
            "smart_bin",
            "smart_bin_name",
            "zone_name",
            "name",
            "sensor_type",
            "serial_number",
            "firmware_version",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "smart_bin_name",
            "zone_name",
            "created_at",
            "updated_at",
        )


class SensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            "smart_bin",
            "name",
            "sensor_type",
            "serial_number",
            "firmware_version",
            "is_active",
        )


class SensorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            "name",
            "firmware_version",
            "is_active",
        )


# ============================================================================
# Sensor Reading
# ============================================================================

class SensorReadingSerializer(serializers.ModelSerializer):
    sensor_name = serializers.CharField(
        source="sensor.name",
        read_only=True,
    )

    sensor_type = serializers.CharField(
        source="sensor.sensor_type",
        read_only=True,
    )

    smart_bin_name = serializers.CharField(
        source="sensor.smart_bin.name",
        read_only=True,
    )

    class Meta:
        model = SensorReading
        fields = (
            "id",
            "sensor",
            "sensor_name",
            "sensor_type",
            "smart_bin_name",
            "value",
            "unit",
            "recorded_at",
            "raw_data",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "sensor_name",
            "sensor_type",
            "smart_bin_name",
            "recorded_at",
            "created_at",
            "updated_at",
        )


class SensorReadingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = (
            "sensor",
            "value",
            "unit",
            "raw_data",
        )


class SensorReadingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = (
            "value",
            "unit",
            "raw_data",
        )