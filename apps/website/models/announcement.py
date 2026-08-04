
from django.db import models

from apps.common.models import BaseModel
from apps.website.choices import AnnouncementStatus


class Announcement(BaseModel):
    title = models.CharField(max_length=255)

    content = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=AnnouncementStatus.choices,
        default=AnnouncementStatus.DRAFT,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title