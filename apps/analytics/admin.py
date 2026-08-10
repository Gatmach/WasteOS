from django.contrib import admin

from .models import KPISnapshot


@admin.register(KPISnapshot)
class KPISnapshotAdmin(admin.ModelAdmin):
    list_display = (
        "period",
        "snapshot_date",
        "total_bins",
        "active_bins",
        "collections_completed",
        "waste_collected_kg",
        "created_at",
    )

    list_filter = (
        "snapshot_date",
        "period",
    )
    search_fields = (
        "period",
    )
    ordering = (
        "-snapshot_date",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 25