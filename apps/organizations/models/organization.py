from django.db import models

from apps.common.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,    
        )

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    address = models.TextField(blank=True)

    is_active = models.BooleanField(
        default=True,
        db_index=True,
        )

    class Meta:
        ordering = ("name",)
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name