from django.test import TestCase

from decimal import Decimal
from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.analytics.choices import KPIType
from apps.analytics.models import KPISnapshot
from apps.analytics.services import create_kpi_snapshot


User = get_user_model()


class AnalyticsOverviewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="analytics_test",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_overview_endpoint_returns_200(self):
        url = reverse("analytics-overview")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_overview_contains_expected_fields(self):
        url = reverse("analytics-overview")

        response = self.client.get(url)

        expected_fields = {
            "total_organizations",
            "total_facilities",
            "total_zones",
            "total_bins",
            "active_bins",
            "average_fill_level",
            "average_battery_level",
            "high_fill_bins",
            "full_bins",
            "offline_bins",
            "total_sensors",
            "active_sensors",
            "total_alerts",
            "active_alerts",
            "critical_alerts",
            "total_schedules",
            "completed_collections",
            "pending_collections",
            "cancelled_collections",
            "total_waste_collected_kg",
            "average_waste_collected_kg",
        }

        self.assertEqual(
            set(response.data.keys()),
            expected_fields,
        )


class KPISnapshotTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="snapshot_test",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_create_kpi_snapshot(self):
        snapshot = create_kpi_snapshot(
            period=KPIType.DAILY,
            snapshot_date=date.today(),
        )

        self.assertIsInstance(
            snapshot,
            KPISnapshot,
        )

        self.assertEqual(
            snapshot.period,
            KPIType.DAILY,
        )

        self.assertEqual(
            snapshot.snapshot_date,
            date.today(),
        )

    def test_snapshot_list_endpoint_returns_200(self):
        url = reverse("kpi-snapshot-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )