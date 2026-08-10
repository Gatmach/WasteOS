
from django.db.models import Avg, Count, Sum

from apps.bins.choices import (
    AlertSeverity,
    AlertStatus,
    BinStatus,
)
from apps.bins.models import Alert, SmartBin
from apps.operations.choices import ScheduleStatus
from apps.operations.models import (
    CollectionRecord,
    CollectionSchedule,
)
from apps.sensors.models import Sensor


def get_dashboard_summary():
    """
    Return the main KPIs displayed on the dashboard.
    """

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

    collections = CollectionRecord.objects.filter(
        is_deleted=False,
    )

    return {
        "total_bins": bins.count(),

        "active_bins": bins.filter(
            is_active=True,
        ).count(),

        "full_bins": bins.filter(
            status=BinStatus.FULL,
        ).count(),

        "offline_bins": bins.filter(
            status=BinStatus.OFFLINE,
        ).count(),

        "average_fill_level": bins.aggregate(
            average=Avg("fill_level"),
        )["average"] or 0,

        "total_sensors": sensors.count(),

        "active_sensors": sensors.filter(
            is_active=True,
        ).count(),

        "active_alerts": alerts.filter(
            status=AlertStatus.ACTIVE,
        ).count(),

        "critical_alerts": alerts.filter(
            severity=AlertSeverity.CRITICAL,
        ).count(),

        "pending_collections": schedules.filter(
            status=ScheduleStatus.PENDING,
        ).count(),

        "completed_collections": schedules.filter(
            status=ScheduleStatus.COMPLETED,
        ).count(),

        "total_waste_collected_kg": collections.aggregate(
            total=Sum("weight_collected"),
        )["total"] or 0,
    }


def get_recent_alerts(limit=5):
    """
    Return the most recent alerts.
    """

    return (
        Alert.objects
        .filter(is_deleted=False)
        .select_related("smart_bin")
        .order_by("-triggered_at")[:limit]
    )


def get_bin_statistics():
    """
    Return bin status statistics.
    """

    bins = SmartBin.objects.filter(
        is_deleted=False,
    )

    return {
        "total": bins.count(),

        "empty": bins.filter(
            status=BinStatus.EMPTY,
        ).count(),

        "low": bins.filter(
            status=BinStatus.LOW,
        ).count(),

        "medium": bins.filter(
            status=BinStatus.MEDIUM,
        ).count(),

        "high": bins.filter(
            status=BinStatus.HIGH,
        ).count(),

        "full": bins.filter(
            status=BinStatus.FULL,
        ).count(),

        "offline": bins.filter(
            status=BinStatus.OFFLINE,
        ).count(),
    }


def get_collection_statistics():
    """
    Return collection operation statistics.
    """

    schedules = CollectionSchedule.objects.filter(
        is_deleted=False,
    )

    records = CollectionRecord.objects.filter(
        is_deleted=False,
    )

    return {
        "total_schedules": schedules.count(),

        "pending": schedules.filter(
            status=ScheduleStatus.PENDING,
        ).count(),

        "in_progress": schedules.filter(
            status=ScheduleStatus.IN_PROGRESS,
        ).count(),

        "completed": schedules.filter(
            status=ScheduleStatus.COMPLETED,
        ).count(),

        "cancelled": schedules.filter(
            status=ScheduleStatus.CANCELLED,
        ).count(),

        "total_waste_collected_kg": records.aggregate(
            total=Sum("weight_collected"),
        )["total"] or 0,

        "average_waste_collected_kg": records.aggregate(
            average=Avg("weight_collected"),
        )["average"] or 0,
    }


def get_sensor_statistics():
    """
    Return sensor statistics grouped by sensor type.
    """

    sensors = Sensor.objects.filter(
        is_deleted=False,
    )

    by_type = (
        sensors
        .values("sensor_type")
        .annotate(total=Count("id"))
        .order_by("sensor_type")
    )

    return {
        "total": sensors.count(),

        "active": sensors.filter(
            is_active=True,
        ).count(),

        "inactive": sensors.filter(
            is_active=False,
        ).count(),

        "by_type": list(by_type),
    }