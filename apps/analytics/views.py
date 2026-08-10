from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytics.selectors import get_overview_analytics
from apps.analytics.serializers import (
    KPISnapshotSerializer,
    OverviewAnalyticsSerializer,
)

#kpi snapshot list view and history view
from rest_framework.generics import ListAPIView
from apps.analytics.models import KPISnapshot

class AnalyticsOverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        analytics = get_overview_analytics()

        serializer = OverviewAnalyticsSerializer(
            analytics,
        )

        return Response(serializer.data)


class KPISnapshotListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = KPISnapshotSerializer

    def get_queryset(self):
        return KPISnapshot.objects.filter(
            is_deleted=False,
        )