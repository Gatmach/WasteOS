
from django.urls import path

from apps.analytics.views import (
    KPISnapshotListView,
    AnalyticsOverviewView,
)

urlpatterns = [
    path(
        "overview/",
        AnalyticsOverviewView.as_view(),
        name="analytics-overview",
    ),
    path(
        "snapshots/",
        KPISnapshotListView.as_view(),
        name="kpi-snapshot-list",
    )
]