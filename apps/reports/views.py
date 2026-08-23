#from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .api import ReportSerializer
from .selectors import (
    get_report,
    get_user_reports,
)
from .services import create_report


class ReportListCreateView(generics.ListCreateAPIView):
    """
    List reports or create a new report.
    """

    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_user_reports(self.request.user)

    def perform_create(self, serializer):
        report = create_report(
            name=serializer.validated_data["name"],
            report_type=serializer.validated_data["report_type"],
            generated_by=self.request.user,
        )

        serializer.instance = report


class ReportDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single report.
    """

    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "report_id"

    def get_queryset(self):
        return get_user_reports(self.request.user)