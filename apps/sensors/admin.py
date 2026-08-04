from django.contrib import admin

from .models import Sensor, SensorReading


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "smart_bin",
        "sensor_type",
        "serial_number",
        "firmware_version",
        "is_active",
    )

    search_fields = (
        "name",
        "serial_number",
        "smart_bin__name",
    )

    list_filter = (
        "sensor_type",
        "is_active",
    )

    autocomplete_fields = (
        "smart_bin",
    )

    list_select_related = (
        "smart_bin",
    )

    ordering = (
        "smart_bin",
        "name",
    )

    list_per_page = 25


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = (
        "sensor",
        "value",
        "unit",
        "recorded_at",
    )

    search_fields = (
        "sensor__name",
        "sensor__serial_number",
    )

    list_filter = (
        "sensor__sensor_type",
    )

    autocomplete_fields = (
        "sensor",
    )

    list_select_related = (
        "sensor",
    )

    ordering = (
        "-recorded_at",
    )

    readonly_fields = (
        "recorded_at",
    )

    list_per_page = 50