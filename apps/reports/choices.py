
from django.db import models


class ReportType(models.TextChoices):
    COLLECTION = "collection", "Collection"
    BIN = "bin", "Bin"
    SENSOR = "sensor", "Sensor"
    ALERT = "alert", "Alert"
    ANALYTICS = "analytics", "Analytics"


class ReportStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"