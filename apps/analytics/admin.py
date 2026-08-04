from django.contrib import admin

from .models import KPISnapshot


@admin.register(KPISnapshot)
class KPISnapshotAdmin(admin.ModelAdmin):
    list_display = (
        "snapshot_date",
        "total_bins",
        "active_bins",
        "collections_completed",
        "created_at",
    )

    list_filter = (
        "snapshot_date",
    )

    ordering = (
        "-snapshot_date",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 25