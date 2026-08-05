
from django.db.models import QuerySet

from apps.organizations.models import (
    Facility,
    Organization,
    Zone,
)

# ============================================================================
# Organization Selectors
# ============================================================================

def get_organization(organization_id) -> Organization:
    return Organization.objects.get(pk=organization_id)


def list_organizations() -> QuerySet[Organization]:
    return Organization.objects.all()


def get_active_organizations() -> QuerySet[Organization]:
    return Organization.objects.filter(is_active=True)


# ============================================================================
# Facility Selectors
# ============================================================================

def get_facility(facility_id) -> Facility:
    return Facility.objects.get(pk=facility_id)


def list_facilities() -> QuerySet[Facility]:
    return Facility.objects.select_related("organization")


def get_active_facilities() -> QuerySet[Facility]:
    return Facility.objects.filter(
        is_active=True,
    ).select_related("organization")


def get_facilities_by_organization(
    organization_id,
) -> QuerySet[Facility]:
    return Facility.objects.filter(
        organization_id=organization_id,
    ).select_related("organization")


# ============================================================================
# Zone Selectors
# ============================================================================

def get_zone(zone_id) -> Zone:
    return Zone.objects.get(pk=zone_id)


def list_zones() -> QuerySet[Zone]:
    return Zone.objects.select_related(
        "facility",
        "facility__organization",
    )


def get_active_zones() -> QuerySet[Zone]:
    return Zone.objects.filter(
        is_active=True,
    ).select_related(
        "facility",
        "facility__organization",
    )


def get_zones_by_facility(
    facility_id,
) -> QuerySet[Zone]:
    return Zone.objects.filter(
        facility_id=facility_id,
    ).select_related(
        "facility",
        "facility__organization",
    )