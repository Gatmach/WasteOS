
from django.db import models

from apps.common.models import BaseModel
from apps.organizations.models import Zone


class CollectionRoute(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(blank=True)

    zones = models.ManyToManyField(
        Zone,
        related_name="collection_routes",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name