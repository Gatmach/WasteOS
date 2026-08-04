from django.db import models

from apps.common.models import BaseModel
from apps.bins.models import SmartBin
from apps.ai.choices import PredictionStatus


class Prediction(BaseModel):
    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="predictions",
    )

    predicted_fill_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    confidence_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    predicted_collection_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=PredictionStatus.choices,
        default=PredictionStatus.COMPLETED,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.smart_bin} ({self.predicted_fill_level}%)"