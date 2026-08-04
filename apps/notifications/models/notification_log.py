
from django.db import models

from apps.common.models import BaseModel

from .notification import Notification


class NotificationLog(BaseModel):
    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        related_name="logs",
    )

    response = models.TextField(blank=True)
    is_successful = models.BooleanField(default=True)
    sent_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"Log #{self.pk}"