
from django.db import models

from apps.common.models import BaseModel


class Driver(BaseModel):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(
        max_length=20,
        unique=True,
    )

    license_number = models.CharField(
        max_length=50,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"