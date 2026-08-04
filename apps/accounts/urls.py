from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenRefreshView

from apps.accounts.api import UserViewSet
from apps.accounts.jwt_views import LoginView

from apps.accounts.api import UserViewSet

router = DefaultRouter()
router.register(
    "users",
    UserViewSet,
    basename="users",
)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]