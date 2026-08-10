
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.sensors.api import (
    SensorViewSet,
    SensorReadingViewSet,
)

router = DefaultRouter()

router.register(
    "sensors",
    SensorViewSet,
    basename="sensor",
)

router.register(
    "readings",
    SensorReadingViewSet,
    basename="sensor-reading",
)

urlpatterns = [
    path("", include(router.urls)),
]