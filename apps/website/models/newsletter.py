
from django.db import models

from apps.common.models import BaseModel


class Newsletter(BaseModel):
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email