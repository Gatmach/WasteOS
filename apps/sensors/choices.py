from django.db import models


class SensorType(models.TextChoices):
    ULTRASONIC = "ultrasonic", "Ultrasonic"
    WEIGHT = "weight", "Weight"
    TEMPERATURE = "temperature", "Temperature"
    HUMIDITY = "humidity", "Humidity"
    GPS = "gps", "GPS"
    OTHER = "other", "Other"