
from django.db import models

from apps.common.models import BaseModel
from apps.bins.models import SmartBin

from .collection_schedule import CollectionSchedule


class CollectionRecord(BaseModel):
    schedule = models.ForeignKey(
        CollectionSchedule,
        on_delete=models.CASCADE,
        related_name="records",
    )

    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="collection_records",
    )

    fill_level_before = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    weight_collected = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    collected_at = models.DateTimeField(
        auto_now_add=True,
    )

    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-collected_at"]

    def __str__(self):
        return f"{self.smart_bin} - {self.collected_at}"