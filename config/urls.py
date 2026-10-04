
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),

    path(
        "api/accounts/",
        include("apps.accounts.urls"),
    ),
    path(
        "api-auth/", 
        include("rest_framework.urls")
    ),
    path(
        "api/organizations/",
        include("apps.organizations.urls"),
    ),
    path(
        "api/bins/",
        include("apps.bins.urls"),
    ),
    path(
        "api/sensors/",
        include("apps.sensors.urls"),
    ),
    path(
        "api/operations/",
        include("apps.operations.urls"),
    ),
    path(
        "api/analytics/",
        include("apps.analytics.urls"),
    ),
    path(
        "api/dashboard/",
        include("apps.dashboard.urls"),
    ),
    path(
        "api/reports/",
        include("apps.reports.urls"),
    ),
    path(
        "api/website/",
        include("apps.website.urls"),
    ),
    path(
        "api/notifications/",
        include("apps.notifications.urls"),
    ),
]
