
from django.db import transaction

from apps.analytics.models import KPISnapshot
from apps.analytics.choices import KPIType

from apps.analytics.selectors import get_overview_analytics


@transaction.atomic
def create_kpi_snapshot(
    *,
    period,
    snapshot_date,
):
    """
    Create a KPI snapshot for the specified period and date.
    """

    analytics = get_overview_analytics()

    snapshot = KPISnapshot.objects.create(
        period=period,
        snapshot_date=snapshot_date,
        total_bins=analytics["total_bins"],
        active_bins=analytics["active_bins"],
        collections_completed=analytics["completed_collections"],
        waste_collected_kg=analytics[
            "total_waste_collected_kg"
        ],
        average_fill_level=analytics[
            "average_fill_level"
        ],
    )

    return snapshot