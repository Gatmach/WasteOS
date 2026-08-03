from django.db import models


class BinStatus(models.TextChoices):
    EMPTY = "empty", "Empty"
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    FULL = "full", "Full"
    OFFLINE = "offline", "Offline"


class AlertType(models.TextChoices):
    BIN_FULL = "bin_full", "Bin Full"
    BATTERY_LOW = "battery_low", "Battery Low"
    SENSOR_OFFLINE = "sensor_offline", "Sensor Offline"
    FIRE = "fire", "Fire"
    TAMPER = "tamper", "Tamper"
    GENERAL = "general", "General"


class AlertStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    ACKNOWLEDGED = "acknowledged", "Acknowledged"
    RESOLVED = "resolved", "Resolved"

class AlertSeverity(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    CRITICAL = "critical", "Critical"