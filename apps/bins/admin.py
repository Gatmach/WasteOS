from django.contrib import admin

from .models import SmartBin, Alert


@admin.register(SmartBin)
class SmartBinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "zone",
        "fill_level",
        "battery_level",
        "capacity_liters",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "zone",
        "is_active",
    )

    ordering = ("name",)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "alert_type",
        "status",
        "triggered_at",
    )

    list_filter = (
        "alert_type",
        "status",
    )

    search_fields = (
        "smart_bin__name",
        "title",
    )