from django.db import models
from apps.common.models import BaseModel
from apps.bins.choices import (
    AlertSeverity,
    AlertStatus,
    AlertType,
)
from .smart_bin import SmartBin


class Alert(BaseModel):
    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="alerts",
    )

    alert_type = models.CharField(
        max_length=50,
        choices=AlertType.choices,
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=AlertStatus.choices,
        default=AlertStatus.ACTIVE,
    )

    triggered_at = models.DateTimeField(auto_now_add=True)

    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    severity = models.CharField(
        max_length=20,
        choices=AlertSeverity.choices,
        default=AlertSeverity.MEDIUM,
    )

    class Meta:
        ordering = ("-triggered_at",)
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["severity"]),
            models.Index(fields=["triggered_at"]),
        ]

    def __str__(self):
        return f"{self.smart_bin.name} - {self.title}"