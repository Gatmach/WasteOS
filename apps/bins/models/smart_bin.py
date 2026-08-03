from django.db import models

from apps.bins.choices import BinStatus
from apps.common.models import BaseModel
from apps.organizations.models import Zone


class SmartBin(BaseModel):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name="bins",
    )

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    capacity_liters = models.PositiveIntegerField(default=240)

    fill_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    battery_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100,
    )

    status = models.CharField(
        max_length=20,
        choices=BinStatus.choices,
        default=BinStatus.EMPTY,
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        constraints = [
            models.UniqueConstraint(
                fields=["zone", "code"],
                name="unique_bin_code_per_zone",
            ),
        ]

    def __str__(self):
        return self.name