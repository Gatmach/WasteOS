from django.db import models


class VehicleStatus(models.TextChoices):
    AVAILABLE = "available", "Available"
    IN_SERVICE = "in_service", "In Service"
    MAINTENANCE = "maintenance", "Maintenance"
    OUT_OF_SERVICE = "out_of_service", "Out of Service"


class ScheduleStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"