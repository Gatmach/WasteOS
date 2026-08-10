
from decimal import Decimal
from django.db import models
from django.db.models import Avg, Count, Sum

from apps.bins.choices import AlertSeverity, AlertStatus, BinStatus
from apps.bins.models import Alert, SmartBin
from apps.operations.choices import ScheduleStatus
from apps.operations.models import CollectionRecord, CollectionSchedule
from apps.organizations.models import Facility, Organization, Zone
from apps.sensors.models import Sensor


def get_overview_analytics():
    """
    Return system-wide operational analytics.

    Analytics are calculated from the existing application data.
    Soft-deleted records are excluded.
    """

    organizations = Organization.objects.filter(
        is_deleted=False,
    )

    facilities = Facility.objects.filter(
        is_deleted=False,
    )

    zones = Zone.objects.filter(
        is_deleted=False,
    )

    bins = SmartBin.objects.filter(
        is_deleted=False,
    )

    sensors = Sensor.objects.filter(
        is_deleted=False,
    )

    alerts = Alert.objects.filter(
        is_deleted=False,
    )

    schedules = CollectionSchedule.objects.filter(
        is_deleted=False,
    )

    collection_records = CollectionRecord.objects.filter(
        is_deleted=False,
    )

    bin_stats = bins.aggregate(
        total=Count("id"),
        active=Count("id", filter=models.Q(is_active=True)),
        average_fill=Avg("fill_level"),
        average_battery=Avg("battery_level"),
        high_fill=Count(
            "id",
            filter=models.Q(status=BinStatus.HIGH),
        ),
        full=Count(
            "id",
            filter=models.Q(status=BinStatus.FULL),
        ),
        offline=Count(
            "id",
            filter=models.Q(status=BinStatus.OFFLINE),
        ),
    )

    sensor_stats = sensors.aggregate(
        total=Count("id"),
        active=Count(
            "id",
            filter=models.Q(is_active=True),
        ),
    )

    alert_stats = alerts.aggregate(
        total=Count("id"),
        active=Count(
            "id",
            filter=models.Q(status=AlertStatus.ACTIVE),
        ),
        critical=Count(
            "id",
            filter=models.Q(
                severity=AlertSeverity.CRITICAL,
            ),
        ),
    )

    schedule_stats = schedules.aggregate(
        total=Count("id"),
        completed=Count(
            "id",
            filter=models.Q(
                status=ScheduleStatus.COMPLETED,
            ),
        ),
        pending=Count(
            "id",
            filter=models.Q(
                status=ScheduleStatus.PENDING,
            ),
        ),
        cancelled=Count(
            "id",
            filter=models.Q(
                status=ScheduleStatus.CANCELLED,
            ),
        ),
    )

    collection_stats = collection_records.aggregate(
        total_weight=Sum("weight_collected"),
        average_weight=Avg("weight_collected"),
    )

    return {
        "total_organizations": organizations.count(),
        "total_facilities": facilities.count(),
        "total_zones": zones.count(),

        "total_bins": bin_stats["total"] or 0,
        "active_bins": bin_stats["active"] or 0,
        "average_fill_level": (
            bin_stats["average_fill"]
            if bin_stats["average_fill"] is not None
            else Decimal("0.00")
        ),
        "average_battery_level": (
            bin_stats["average_battery"]
            if bin_stats["average_battery"] is not None
            else Decimal("0.00")
        ),
        "high_fill_bins": bin_stats["high_fill"] or 0,
        "full_bins": bin_stats["full"] or 0,
        "offline_bins": bin_stats["offline"] or 0,

        "total_sensors": sensor_stats["total"] or 0,
        "active_sensors": sensor_stats["active"] or 0,

        "total_alerts": alert_stats["total"] or 0,
        "active_alerts": alert_stats["active"] or 0,
        "critical_alerts": alert_stats["critical"] or 0,

        "total_schedules": schedule_stats["total"] or 0,
        "completed_collections": schedule_stats["completed"] or 0,
        "pending_collections": schedule_stats["pending"] or 0,
        "cancelled_collections": schedule_stats["cancelled"] or 0,

        "total_waste_collected_kg": (
            collection_stats["total_weight"]
            if collection_stats["total_weight"] is not None
            else Decimal("0.00")
        ),
        "average_waste_collected_kg": (
            collection_stats["average_weight"]
            if collection_stats["average_weight"] is not None
            else Decimal("0.00")
        ),
    }