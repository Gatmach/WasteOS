
from django.db.models import QuerySet
from apps.bins.choices import AlertStatus
from apps.bins.models import (
    Alert,
    SmartBin,
)


# ============================================================================
# Smart Bin Selectors
# ============================================================================

def get_smart_bin(smart_bin_id) -> SmartBin:
    return (
        SmartBin.objects
        .select_related(
            "zone",
            "zone__facility",
            "zone__facility__organization",
        )
        .get(pk=smart_bin_id)
    )


def list_smart_bins() -> QuerySet[SmartBin]:
    return SmartBin.objects.select_related(
        "zone",
        "zone__facility",
        "zone__facility__organization",
    )


def get_active_smart_bins() -> QuerySet[SmartBin]:
    return (
        SmartBin.objects.filter(is_active=True)
        .select_related(
            "zone",
            "zone__facility",
            "zone__facility__organization",
        )
    )


def get_smart_bins_by_zone(
    zone_id,
) -> QuerySet[SmartBin]:
    return (
        SmartBin.objects.filter(zone_id=zone_id)
        .select_related(
            "zone",
            "zone__facility",
            "zone__facility__organization",
        )
    )


def get_smart_bins_by_status(
    status,
) -> QuerySet[SmartBin]:
    return (
        SmartBin.objects.filter(status=status)
        .select_related(
            "zone",
            "zone__facility",
            "zone__facility__organization",
        )
    )


# ============================================================================
# Alert Selectors
# ============================================================================

def get_alert(alert_id) -> Alert:
    return (
        Alert.objects
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
        .get(pk=alert_id)
    )


def list_alerts() -> QuerySet[Alert]:
    return Alert.objects.select_related(
        "smart_bin",
        "smart_bin__zone",
        "smart_bin__zone__facility",
        "smart_bin__zone__facility__organization",
    )


def get_active_alerts() -> QuerySet[Alert]:
    return (
        Alert.objects.filter(status=AlertStatus.ACTIVE)
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
    )


def get_alerts_by_bin(
    smart_bin_id,
) -> QuerySet[Alert]:
    return (
        Alert.objects.filter(
            smart_bin_id=smart_bin_id,
        )
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
    )


def get_alerts_by_status(
    status,
) -> QuerySet[Alert]:
    return (
        Alert.objects.filter(status=status)
        .select_related(
            "smart_bin",
            "smart_bin__zone",
            "smart_bin__zone__facility",
            "smart_bin__zone__facility__organization",
        )
    )