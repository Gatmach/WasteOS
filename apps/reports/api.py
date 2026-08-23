
from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    generated_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            "id",
            "name",
            "report_type",
            "status",
            "generated_by",
            "generated_by_name",
            "file",
            "generated_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "generated_by",
            "generated_by_name",
            "generated_at",
            "file",
            "created_at",
            "updated_at",
        ]

    def get_generated_by_name(self, obj):
        if not obj.generated_by:
            return None

        return obj.generated_by.full_name

