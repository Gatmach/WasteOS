
from rest_framework import serializers


class DashboardSummarySerializer(serializers.Serializer):
    total_bins = serializers.IntegerField()
    active_bins = serializers.IntegerField()
    full_bins = serializers.IntegerField()
    offline_bins = serializers.IntegerField()
    average_fill_level = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    total_sensors = serializers.IntegerField()
    active_sensors = serializers.IntegerField()

    active_alerts = serializers.IntegerField()
    critical_alerts = serializers.IntegerField()

    pending_collections = serializers.IntegerField()
    completed_collections = serializers.IntegerField()

    total_waste_collected_kg = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class BinStatisticsSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    empty = serializers.IntegerField()
    low = serializers.IntegerField()
    medium = serializers.IntegerField()
    high = serializers.IntegerField()
    full = serializers.IntegerField()
    offline = serializers.IntegerField()


class CollectionStatisticsSerializer(serializers.Serializer):
    total_schedules = serializers.IntegerField()
    pending = serializers.IntegerField()
    in_progress = serializers.IntegerField()
    completed = serializers.IntegerField()
    cancelled = serializers.IntegerField()

    total_waste_collected_kg = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    average_waste_collected_kg = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )


class SensorTypeStatisticsSerializer(serializers.Serializer):
    sensor_type = serializers.CharField()
    total = serializers.IntegerField()


class SensorStatisticsSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    active = serializers.IntegerField()
    inactive = serializers.IntegerField()

    by_type = SensorTypeStatisticsSerializer(
        many=True,
    )


class RecentAlertSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    message = serializers.CharField()
    alert_type = serializers.CharField()
    severity = serializers.CharField()
    status = serializers.CharField()
    triggered_at = serializers.DateTimeField()

    smart_bin = serializers.SerializerMethodField()

    def get_smart_bin(self, obj):
        return {
            "id": obj.smart_bin.id,
            "name": obj.smart_bin.name,
            "code": obj.smart_bin.code,
        }