from django.db import models

from apps.common.models import BaseModel

from .sensor import Sensor


class SensorReading(BaseModel):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="readings",
    )

    value = models.FloatField()

    unit = models.CharField(
        max_length=20,
        blank=True,
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True,
    )
    raw_data = models.JSONField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-recorded_at",)
        verbose_name = "Sensor Reading"
        verbose_name_plural = "Sensor Readings"

    def __str__(self):
        return (
            f"{self.sensor.name}: "
            f"{self.value} {self.unit}".strip()
        )