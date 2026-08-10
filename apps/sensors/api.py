
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import IsSuperAdmin
from rest_framework import mixins, viewsets
from apps.sensors.selectors import (
    list_sensors,
    list_sensor_readings,
)

from apps.sensors.serializers import (
    SensorSerializer,
    SensorCreateSerializer,
    SensorUpdateSerializer,
    SensorReadingSerializer,
    SensorReadingCreateSerializer,
    SensorReadingUpdateSerializer,
)

from apps.sensors.services import (
    create_sensor,
    update_sensor,
    create_sensor_reading,
    update_sensor_reading,
)


class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_sensors()

    def get_serializer_class(self):
        if self.action == "create":
            return SensorCreateSerializer

        if self.action in ("update", "partial_update"):
            return SensorUpdateSerializer

        return SensorSerializer

    def perform_create(self, serializer):
        serializer.instance = create_sensor(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_sensor(
            serializer.instance,
            **serializer.validated_data,
        )

class SensorReadingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    ):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_sensor_readings()

    def get_serializer_class(self):
        if self.action == "create":
            return SensorReadingCreateSerializer

        if self.action in ("update", "partial_update"):
            return SensorReadingUpdateSerializer

        return SensorReadingSerializer

    def perform_create(self, serializer):
        serializer.instance = create_sensor_reading(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_sensor_reading(
            serializer.instance,
            **serializer.validated_data,
        )