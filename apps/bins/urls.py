
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.bins.api import (
    AlertViewSet,
    SmartBinViewSet,
)

router = DefaultRouter()

router.register(
    "smart-bins",
    SmartBinViewSet,
    basename="smart-bin",
)

router.register(
    "alerts",
    AlertViewSet,
    basename="alert",
)

urlpatterns = [
    path("", include(router.urls)),
]