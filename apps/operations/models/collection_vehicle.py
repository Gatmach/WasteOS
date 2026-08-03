from django.db import models

from apps.common.models import BaseModel
from apps.operations.choices import VehicleStatus


class CollectionVehicle(BaseModel):
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
    )

    name = models.CharField(
        max_length=100,
    )

    capacity_kg = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=VehicleStatus.choices,
        default=VehicleStatus.AVAILABLE,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["registration_number"]
        verbose_name = "Collection Vehicle"
        verbose_name_plural = "Collection Vehicles"

    def __str__(self):
        return f"{self.registration_number} - {self.name}"