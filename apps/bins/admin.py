from django.contrib import admin
from .models import Alert, SmartBin
from apps.bins.choices import BinStatus

@admin.register(SmartBin)
class SmartBinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "zone",
        "fill_level",
        "battery_level",
        "status",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "zone__name",
    )

    list_filter = (
        "status",
        "zone",
        "is_active",
    )

    autocomplete_fields = (
        "zone",
    )

    list_select_related = (
        "zone",
    )

    ordering = (
        "zone",
        "name",
    )

    list_per_page = 25


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "smart_bin",
        "alert_type",
        "status",
        "triggered_at",
    )

    search_fields = (
        "title",
        "message",
        "smart_bin__name",
    )

    list_filter = (
        "alert_type",
        "status",
    )

    autocomplete_fields = (
        "smart_bin",
    )

    list_select_related = (
        "smart_bin",
    )

    ordering = (
        "-triggered_at",
    )

    readonly_fields = (
        "triggered_at",
        "resolved_at",
    )

    list_per_page = 25