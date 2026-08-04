
from django.db import models

from apps.accounts.models import User
from apps.common.models import BaseModel
from apps.reports.choices import (
    ReportStatus,
    ReportType,
)


class Report(BaseModel):
    name = models.CharField(max_length=255)

    report_type = models.CharField(
        max_length=30,
        choices=ReportType.choices,
    )

    generated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reports",
    )

    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.PENDING,
    )

    file = models.FileField(
        upload_to="reports/",
        blank=True,
        null=True,
    )

    generated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return self.name