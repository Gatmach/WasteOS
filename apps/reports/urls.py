
from django.urls import path

from .views import (
    ReportDetailView,
    ReportListCreateView,
)


urlpatterns = [
    path(
        "",
        ReportListCreateView.as_view(),
        name="report-list-create",
    ),
    path(
        "<uuid:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail",
    ),
]