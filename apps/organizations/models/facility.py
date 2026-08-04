from django.db import models

from apps.common.models import BaseModel
from apps.organizations.choices import FacilityType

from .organization import Organization


class Facility(BaseModel):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="facilities",
    )

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50)

    facility_type = models.CharField(
        max_length=30,
        choices=FacilityType.choices,
        default=FacilityType.UNIVERSITY,
    )

    address = models.TextField(blank=True)

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
                fields=["organization", "code"],
                name="unique_facility_code_per_organization",
            ),
        ]

    def __str__(self):
        return self.name