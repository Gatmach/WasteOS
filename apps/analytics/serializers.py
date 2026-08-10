
from rest_framework import serializers
from apps.analytics.models import KPISnapshot

class OverviewAnalyticsSerializer(serializers.Serializer):
    total_organizations = serializers.IntegerField()
    total_facilities = serializers.IntegerField()
    total_zones = serializers.IntegerField()

    total_bins = serializers.IntegerField()
    active_bins = serializers.IntegerField()
    average_fill_level = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    average_battery_level = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    high_fill_bins = serializers.IntegerField()
    full_bins = serializers.IntegerField()
    offline_bins = serializers.IntegerField()

    total_sensors = serializers.IntegerField()
    active_sensors = serializers.IntegerField()

    total_alerts = serializers.IntegerField()
    active_alerts = serializers.IntegerField()
    critical_alerts = serializers.IntegerField()

    total_schedules = serializers.IntegerField()
    completed_collections = serializers.IntegerField()
    pending_collections = serializers.IntegerField()
    cancelled_collections = serializers.IntegerField()

    total_waste_collected_kg = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    average_waste_collected_kg = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

class KPISnapshotSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = KPISnapshot
        fields = [
            "id",
            "period",
            "total_bins",
            "active_bins",
            "collections_completed",
            "waste_collected_kg",
            "average_fill_level",
            "snapshot_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]