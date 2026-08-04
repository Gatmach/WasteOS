from django.db import models


class NotificationType(models.TextChoices):
    ALERT = "alert", "Alert"
    REMINDER = "reminder", "Reminder"
    SYSTEM = "system", "System"
    AI = "ai", "AI Recommendation"


class NotificationChannel(models.TextChoices):
    IN_APP = "in_app", "In-App"
    EMAIL = "email", "Email"
    SMS = "sms", "SMS"


class NotificationStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    SENT = "sent", "Sent"
    FAILED = "failed", "Failed"
    READ = "read", "Read"