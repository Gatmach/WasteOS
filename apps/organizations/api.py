
from apps.organizations.selectors import (
    list_organizations,
    list_facilities,
    list_zones,
)
from apps.organizations.serializers import (
    OrganizationSerializer,
    OrganizationCreateSerializer,
    OrganizationUpdateSerializer,
    FacilitySerializer,
    FacilityCreateSerializer,
    FacilityUpdateSerializer,
    ZoneSerializer,
    ZoneCreateSerializer,
    ZoneUpdateSerializer,
)
from apps.organizations.services import (
    create_organization,
    update_organization,
    create_facility,
    update_facility,
    create_zone,
    update_zone,
)

from apps.common.api import BaseAdminModelViewSet

# ============================================================================
# Organization
# ============================================================================

class OrganizationViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    ordering_fields = (
        "name",
        "created_at",
    )

    ordering = (
        "name",
    )

    def get_queryset(self):
        return list_organizations()

    def get_serializer_class(self):
        if self.action == "create":
            return OrganizationCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return OrganizationUpdateSerializer

        return OrganizationSerializer

    def perform_create(self, serializer):
        serializer.instance = create_organization(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_organization(
            serializer.instance,
            **serializer.validated_data,
        )


# ============================================================================
# Facility
# ============================================================================

class FacilityViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "organization",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    ordering_fields = (
        "name",
        "created_at",
    )

    ordering = (
        "name",
    )

    def get_queryset(self):
        return list_facilities()

    def get_serializer_class(self):
        if self.action == "create":
            return FacilityCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return FacilityUpdateSerializer

        return FacilitySerializer

    def perform_create(self, serializer):
        serializer.instance = create_facility(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_facility(
            serializer.instance,
            **serializer.validated_data,
        )


# ============================================================================
# Zone
# ============================================================================

class ZoneViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "facility",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    ordering_fields = (
        "name",
        "created_at",
    )

    ordering = (
        "name",
    )

    def get_queryset(self):
        return list_zones()

    def get_serializer_class(self):
        if self.action == "create":
            return ZoneCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return ZoneUpdateSerializer

        return ZoneSerializer

    def perform_create(self, serializer):
        serializer.instance = create_zone(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_zone(
            serializer.instance,
            **serializer.validated_data,
        )