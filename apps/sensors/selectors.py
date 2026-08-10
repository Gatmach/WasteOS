
from django.db.models import QuerySet

from apps.sensors.models import (
    Sensor,
    SensorReading,
)


# ============================================================================
# Sensor Selectors
# ============================================================================

def get_sensor(sensor_id) -> Sensor:
    return (
        Sensor.objects
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
        .get(pk=sensor_id)
    )


def list_sensors() -> QuerySet[Sensor]:
    return Sensor.objects.select_related(
        "smart_bin",
        "smart_bin__zone",
        "smart_bin__zone__facility",
        "smart_bin__zone__facility__organization",
    )


def get_active_sensors() -> QuerySet[Sensor]:
    return (
        Sensor.objects.filter(is_active=True)
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
    )


def get_sensors_by_bin(
    smart_bin_id,
) -> QuerySet[Sensor]:
    return (
        Sensor.objects.filter(
            smart_bin_id=smart_bin_id,
        )
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
    )


# ============================================================================
# Sensor Reading Selectors
# ============================================================================

def get_sensor_reading(reading_id) -> SensorReading:
    return (
        SensorReading.objects
        .select_related(
            "sensor",
            "sensor__smart_bin",
            "sensor__smart_bin__zone",
        )
        .get(pk=reading_id)
    )


def list_sensor_readings() -> QuerySet[SensorReading]:
    return SensorReading.objects.select_related(
        "sensor",
        "sensor__smart_bin",
        "sensor__smart_bin__zone",
    )


def get_readings_by_sensor(
    sensor_id,
) -> QuerySet[SensorReading]:
    return (
        SensorReading.objects.filter(
            sensor_id=sensor_id,
        )
        .select_related(
            "sensor",
            "sensor__smart_bin",
            "sensor__smart_bin__zone",
        )
    )