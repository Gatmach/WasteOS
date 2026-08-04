
from django.db import models

from apps.common.models import BaseModel


class FAQ(BaseModel):
    question = models.CharField(max_length=255)

    answer = models.TextField()

    is_active = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.question