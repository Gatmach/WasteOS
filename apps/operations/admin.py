from django.contrib import admin

from .models import (
    CollectionRecord,
    CollectionRoute,
    CollectionSchedule,
    CollectionVehicle,
    Driver,
)


@admin.register(CollectionVehicle)
class CollectionVehicleAdmin(admin.ModelAdmin):
    list_display = (
        "registration_number",
        "name",
        "capacity_kg",
        "status",
        "is_active",
    )

    search_fields = (
        "registration_number",
        "name",
    )

    list_filter = (
        "status",
        "is_active",
    )

    ordering = (
        "registration_number",
    )

    list_per_page = 25


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "license_number",
        "is_active",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone_number",
        "license_number",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "first_name",
        "last_name",
    )

    list_per_page = 25


@admin.register(CollectionRoute)
class CollectionRouteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    filter_horizontal = (
        "zones",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "route",
        "vehicle",
        "driver",
        "scheduled_date",
        "scheduled_time",
        "status",
    )

    search_fields = (
        "route__name",
        "vehicle__registration_number",
        "driver__first_name",
        "driver__last_name",
    )

    list_filter = (
        "status",
        "scheduled_date",
    )

    autocomplete_fields = (
        "route",
        "vehicle",
        "driver",
    )

    list_select_related = (
        "route",
        "vehicle",
        "driver",
    )

    ordering = (
        "-scheduled_date",
        "-scheduled_time",
    )

    list_per_page = 25


@admin.register(CollectionRecord)
class CollectionRecordAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "schedule",
        "fill_level_before",
        "weight_collected",
        "collected_at",
    )

    search_fields = (
        "smart_bin__name",
        "schedule__route__name",
    )

    autocomplete_fields = (
        "schedule",
        "smart_bin",
    )

    list_select_related = (
        "schedule",
        "smart_bin",
    )

    readonly_fields = (
        "collected_at",
    )

    ordering = (
        "-collected_at",
    )

    list_per_page = 50