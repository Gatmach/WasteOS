from django.contrib import admin

from .models import Forecast, Prediction, Recommendation


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "predicted_fill_level",
        "confidence_score",
        "predicted_collection_time",
        "created_at",
    )

    search_fields = (
        "smart_bin__name",
    )

    list_filter = (
        "predicted_collection_time",
    )

    autocomplete_fields = (
        "smart_bin",
    )

    list_select_related = (
        "smart_bin",
    )

    ordering = (
        "predicted_collection_time",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 25


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "forecast_date",
        "expected_fill_level",
        "created_at",
    )

    search_fields = (
        "smart_bin__name",
    )

    list_filter = (
        "forecast_date",
    )

    autocomplete_fields = (
        "smart_bin",
    )

    list_select_related = (
        "smart_bin",
    )

    ordering = (
        "-forecast_date",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 25


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        "smart_bin",
        "priority",
        "is_resolved",
        "created_at",
    )

    search_fields = (
        "smart_bin__name",
    )

    list_filter = (
        "priority",
        "is_resolved",
    )

    autocomplete_fields = (
        "smart_bin",
    )

    list_select_related = (
        "smart_bin",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 25