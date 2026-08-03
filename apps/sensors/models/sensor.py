from django.db import models

from apps.bins.models import SmartBin
from apps.common.models import BaseModel
from apps.sensors.choices import SensorType


class Sensor(BaseModel):
    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="sensors",
    )

    name = models.CharField(max_length=100)

    sensor_type = models.CharField(
        max_length=30,
        choices=SensorType.choices,
    )

    serial_number = models.CharField(
        max_length=100,
        unique=True,
    )

    firmware_version = models.CharField(
        max_length=50,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Sensor"
        verbose_name_plural = "Sensors"

    def __str__(self):
        return f"{self.name} ({self.get_sensor_type_display()})"