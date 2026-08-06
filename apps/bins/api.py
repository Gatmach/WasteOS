
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import IsSuperAdmin

from apps.bins.selectors import (
    list_smart_bins,
    list_alerts,
)

from apps.bins.serializers import (
    SmartBinSerializer,
    SmartBinCreateSerializer,
    SmartBinUpdateSerializer,
    AlertSerializer,
    AlertCreateSerializer,
    AlertUpdateSerializer,
)

from apps.bins.services import (
    create_smart_bin,
    update_smart_bin,
    create_alert,
    update_alert,
)


# ============================================================================
# Smart Bin
# ============================================================================

class SmartBinViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_smart_bins()

    def get_serializer_class(self):
        if self.action == "create":
            return SmartBinCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return SmartBinUpdateSerializer

        return SmartBinSerializer

    def perform_create(self, serializer):
        serializer.instance = create_smart_bin(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_smart_bin(
            serializer.instance,
            **serializer.validated_data,
        )


# ============================================================================
# Alert
# ============================================================================

class AlertViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_alerts()

    def get_serializer_class(self):
        if self.action == "create":
            return AlertCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return AlertUpdateSerializer

        return AlertSerializer

    def perform_create(self, serializer):
        serializer.instance = create_alert(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_alert(
            serializer.instance,
            **serializer.validated_data,
        )