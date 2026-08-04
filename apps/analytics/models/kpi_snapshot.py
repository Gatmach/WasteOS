from django.db import models

from apps.analytics.choices import KPIType
from apps.common.models import BaseModel


class KPISnapshot(BaseModel):
    period = models.CharField(
        max_length=20,
        choices=KPIType.choices,
    )

    total_bins = models.PositiveIntegerField(default=0)

    active_bins = models.PositiveIntegerField(default=0)

    collections_completed = models.PositiveIntegerField(default=0)

    waste_collected_kg = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    average_fill_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )

    snapshot_date = models.DateField()

    class Meta:
        ordering = ["-snapshot_date"]
        verbose_name = "KPI Snapshot"
        verbose_name_plural = "KPI Snapshots"

    def __str__(self):
        return f"{self.period} - {self.snapshot_date}"