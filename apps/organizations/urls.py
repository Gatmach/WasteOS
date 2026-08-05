
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.organizations.api import (
    FacilityViewSet,
    OrganizationViewSet,
    ZoneViewSet,
)

router = DefaultRouter()

router.register(
    "organizations",
    OrganizationViewSet,
    basename="organization",
)

router.register(
    "facilities",
    FacilityViewSet,
    basename="facility",
)

router.register(
    "zones",
    ZoneViewSet,
    basename="zone",
)

urlpatterns = [
    path("", include(router.urls)),
]