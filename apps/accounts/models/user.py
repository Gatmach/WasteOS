from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.choices import UserRole
from apps.common.models import BaseModel
from apps.organizations.models import Facility, Organization


class User(AbstractUser, BaseModel):
    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
        unique=True,
    )

    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.VIEWER,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        related_name="users",
        null=True,
        blank=True,
    )

    facility = models.ForeignKey(
        Facility,
        on_delete=models.SET_NULL,
        related_name="users",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def full_name(self):
        return self.get_full_name()