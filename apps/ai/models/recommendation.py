
from django.db import models

from apps.common.models import BaseModel
from apps.bins.models import SmartBin
from apps.ai.choices import RecommendationPriority


class Recommendation(BaseModel):
    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="recommendations",
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=RecommendationPriority.choices,
        default=RecommendationPriority.MEDIUM,
    )

    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title