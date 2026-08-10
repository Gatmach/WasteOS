from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.operations.api import DriverViewSet

router = DefaultRouter()

router.register(
    "drivers",
    DriverViewSet,
    basename="driver",
)

urlpatterns = [
    path("", include(router.urls)),
]