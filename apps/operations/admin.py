from django.contrib import admin

from .models import (
    CollectionVehicle,
    Driver,
    CollectionRoute,
    CollectionSchedule,
    CollectionRecord,
)


@admin.register(CollectionVehicle)
class CollectionVehicleAdmin(admin.ModelAdmin):
    list_display = (
        "registration_number",
        "name",
        "status",
        "capacity_kg",
        "is_active",
    )
    list_filter = ("status", "is_active")
    search_fields = ("registration_number", "name")


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
        "license_number",
    )


@admin.register(CollectionRoute)
class CollectionRouteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )
    search_fields = ("name",)


@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "route",
        "vehicle",
        "driver",
        "scheduled_date",
        "status",
    )
    list_filter = (
        "status",
        "scheduled_date",
    )


@admin.register(CollectionRecord)
class CollectionRecordAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "schedule",
        "weight_collected",
        "collected_at",
    )
    list_filter = ("collected_at",)