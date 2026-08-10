
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.views import APIView

from apps.dashboard.selectors import (
    get_bin_statistics,
    get_collection_statistics,
    get_dashboard_summary,
    get_recent_alerts,
    get_sensor_statistics,
)
from apps.dashboard.serializers import (
    BinStatisticsSerializer,
    CollectionStatisticsSerializer,
    DashboardSummarySerializer,
    RecentAlertSerializer,
    SensorStatisticsSerializer,
)


class DashboardOverviewView(APIView):
    """
    Return the main dashboard overview.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        summary = get_dashboard_summary()
        bins = get_bin_statistics()
        collections = get_collection_statistics()
        sensors = get_sensor_statistics()
        recent_alerts = get_recent_alerts()

        return Response(
            {
                "summary": DashboardSummarySerializer(
                    summary,
                ).data,

                "bins": BinStatisticsSerializer(
                    bins,
                ).data,

                "collections": CollectionStatisticsSerializer(
                    collections,
                ).data,

                "sensors": SensorStatisticsSerializer(
                    sensors,
                ).data,

                "recent_alerts": RecentAlertSerializer(
                    recent_alerts,
                    many=True,
                ).data,
            }
        )