
from django.db import transaction

from apps.organizations.models import (
    Organization,
    Facility,
    Zone,
)

# ============================================================================
# Organization Services
# ============================================================================

@transaction.atomic
def create_organization(**validated_data) -> Organization:
    organization = Organization.objects.create(
        **validated_data,
    )

    return organization


@transaction.atomic
def update_organization(
    organization: Organization,
    **validated_data,
) -> Organization:
    for field, value in validated_data.items():
        setattr(organization, field, value)

    organization.save()

    return organization


@transaction.atomic
def activate_organization(
    organization: Organization,
) -> Organization:
    organization.is_active = True
    organization.save(
        update_fields=["is_active"],
    )

    return organization


@transaction.atomic
def deactivate_organization(
    organization: Organization,
) -> Organization:
    organization.is_active = False
    organization.save(
        update_fields=["is_active"],
    )

    return organization


# ============================================================================
# Facility Services
# ============================================================================

@transaction.atomic
def create_facility(**validated_data) -> Facility:
    facility = Facility.objects.create(
        **validated_data,
    )

    return facility


@transaction.atomic
def update_facility(
    facility: Facility,
    **validated_data,
) -> Facility:
    for field, value in validated_data.items():
        setattr(facility, field, value)

    facility.save()

    return facility


@transaction.atomic
def activate_facility(
    facility: Facility,
) -> Facility:
    facility.is_active = True
    facility.save(
        update_fields=["is_active"],
    )

    return facility


@transaction.atomic
def deactivate_facility(
    facility: Facility,
) -> Facility:
    facility.is_active = False
    facility.save(
        update_fields=["is_active"],
    )

    return facility


# ============================================================================
# Zone Services
# ============================================================================

@transaction.atomic
def create_zone(**validated_data) -> Zone:
    zone = Zone.objects.create(
        **validated_data,
    )

    return zone


@transaction.atomic
def update_zone(
    zone: Zone,
    **validated_data,
) -> Zone:
    for field, value in validated_data.items():
        setattr(zone, field, value)

    zone.save()

    return zone


@transaction.atomic
def activate_zone(
    zone: Zone,
) -> Zone:
    zone.is_active = True
    zone.save(
        update_fields=["is_active"],
    )

    return zone


@transaction.atomic
def deactivate_zone(
    zone: Zone,
) -> Zone:
    zone.is_active = False
    zone.save(
        update_fields=["is_active"],
    )

    return zone