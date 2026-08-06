
from django.db import transaction
from apps.bins.choices import AlertStatus
from apps.bins.models import (
    Alert,
    SmartBin,
)

# ============================================================================
# Smart Bin Services
# ============================================================================

@transaction.atomic
def create_smart_bin(**validated_data) -> SmartBin:
    return SmartBin.objects.create(**validated_data)


@transaction.atomic
def update_smart_bin(
    smart_bin: SmartBin,
    **validated_data,
) -> SmartBin:
    for field, value in validated_data.items():
        setattr(smart_bin, field, value)

    smart_bin.save()

    return smart_bin


@transaction.atomic
def activate_smart_bin(
    smart_bin: SmartBin,
) -> SmartBin:
    smart_bin.is_active = True
    smart_bin.save(update_fields=["is_active"])

    return smart_bin


@transaction.atomic
def deactivate_smart_bin(
    smart_bin: SmartBin,
) -> SmartBin:
    smart_bin.is_active = False
    smart_bin.save(update_fields=["is_active"])

    return smart_bin


# ============================================================================
# Alert Services
# ============================================================================

@transaction.atomic
def create_alert(**validated_data) -> Alert:
    return Alert.objects.create(**validated_data)


@transaction.atomic
def update_alert(
    alert: Alert,
    **validated_data,
) -> Alert:
    for field, value in validated_data.items():
        setattr(alert, field, value)

    alert.save()

    return alert


@transaction.atomic
def resolve_alert(alert: Alert) -> Alert:
    from django.utils import timezone

    alert.status = AlertStatus.RESOLVED
    alert.resolved_at = timezone.now()

    alert.save(
        update_fields=[
            "status",
            "resolved_at",
        ]
    )

    return alert


@transaction.atomic
def activate_alert(
    alert: Alert,
) -> Alert:
    alert.status = AlertStatus.ACTIVE

    alert.save(update_fields=["status"])

    return alert