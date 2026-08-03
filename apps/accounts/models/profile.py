
from django.db import models

from apps.common.models import BaseModel
from .user import User


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    avatar = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    emergency_contact = models.CharField(
        max_length=100,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f"{self.user.full_name}'s Profile"