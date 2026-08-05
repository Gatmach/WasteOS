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
        "email",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
        "code",
        "facility_type",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "organization__name",
    )

    list_filter = (
        "facility_type",
        "organization",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
    )

    list_select_related = (
        "organization",
    )

    ordering = (
        "organization",
        "name",
    )

    list_per_page = 25


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "facility",
        "code",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "facility__name",
    )

    list_filter = (
        "facility",
        "is_active",
    )

    autocomplete_fields = (
        "facility",
    )

    list_select_related = (
        "facility",
    )

    ordering = (
        "facility",
        "name",
    )

    list_per_page = 25