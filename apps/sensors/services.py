
from django.db import transaction

from apps.sensors.models import (
    Sensor,
    SensorReading,
)


# ============================================================================
# Sensor Services
# ============================================================================

@transaction.atomic
def create_sensor(**validated_data) -> Sensor:
    return Sensor.objects.create(**validated_data)


@transaction.atomic
def update_sensor(
    sensor: Sensor,
    **validated_data,
) -> Sensor:
    for field, value in validated_data.items():
        setattr(sensor, field, value)

    sensor.save()

    return sensor


@transaction.atomic
def activate_sensor(sensor: Sensor) -> Sensor:
    sensor.is_active = True
    sensor.save(update_fields=["is_active"])

    return sensor


@transaction.atomic
def deactivate_sensor(sensor: Sensor) -> Sensor:
    sensor.is_active = False
    sensor.save(update_fields=["is_active"])

    return sensor


# ============================================================================
# Sensor Reading Services
# ============================================================================

@transaction.atomic
def create_sensor_reading(**validated_data) -> SensorReading:
    return SensorReading.objects.create(**validated_data)


@transaction.atomic
def update_sensor_reading(
    reading: SensorReading,
    **validated_data,
) -> SensorReading:
    for field, value in validated_data.items():
        setattr(reading, field, value)

    reading.save()

    return reading