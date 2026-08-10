

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.accounts.permissions import IsSuperAdmin

from apps.operations.serializers import (
    DriverSerializer,
    DriverCreateSerializer,
    DriverUpdateSerializer,
)

from apps.operations.selectors import (
    list_drivers,
)

from apps.operations.services import (
    create_driver,
    update_driver,
)


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_drivers()

    def get_serializer_class(self):
        if self.action == "create":
            return DriverCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return DriverUpdateSerializer

        return DriverSerializer

    def perform_create(self, serializer):
        serializer.instance = create_driver(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_driver(
            serializer.instance,
            **serializer.validated_data,
        )