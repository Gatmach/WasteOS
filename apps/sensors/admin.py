
from django.contrib import admin

from .models import Sensor, SensorReading


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sensor_type",
        "smart_bin",
        "serial_number",
        "is_active",
    )

    list_filter = (
        "sensor_type",
        "is_active",
    )

    search_fields = (
        "name",
        "serial_number",
    )

@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = (
        "sensor",
        "value",
        "unit",
        "recorded_at",
    )

    list_filter = (
        "sensor",
    )

    search_fields = (
        "sensor__name",
    )