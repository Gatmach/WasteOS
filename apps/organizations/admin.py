from django.contrib import admin

from .models import Organization, Facility, Zone


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "email",
        "phone",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("organization", "is_active")

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "facility", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("facility", "is_active")