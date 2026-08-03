from django.db import models

from apps.common.models import BaseModel
from .facility import Facility


class Zone(BaseModel):
    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="zones",
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["facility", "code"],
                name="unique_zone_code_per_facility",
            ),
        ]

    def __str__(self):
        return f"{self.facility.name} - {self.name}"