from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "report_type",
        "generated_by",
        "status",
        "generated_at",
    )

    search_fields = (
        "name",
        "generated_by__username",
    )

    list_filter = (
        "report_type",
        "status",
    )

    autocomplete_fields = (
        "generated_by",
    )

    list_select_related = (
        "generated_by",
    )

    ordering = (
        "-generated_at",
    )

    readonly_fields = (
        "generated_at",
    )

    list_per_page = 25