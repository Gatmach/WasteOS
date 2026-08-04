
from django.db import models

from apps.common.models import BaseModel
from apps.website.choices import MessageStatus


class ContactMessage(BaseModel):
    name = models.CharField(max_length=255)

    email = models.EmailField()

    subject = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=MessageStatus.choices,
        default=MessageStatus.NEW,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject