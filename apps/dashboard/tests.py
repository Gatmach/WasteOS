from django.test import TestCase

from decimal import Decimal
from datetime import date, time

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.bins.choices import (
    AlertSeverity,
    AlertStatus,
    AlertType,
    BinStatus,
)
from apps.bins.models import Alert, SmartBin
from apps.operations.choices import ScheduleStatus
from apps.operations.models import (
    CollectionRecord,
    CollectionRoute,
    CollectionSchedule,
    CollectionVehicle,
    Driver,
)
from apps.organizations.models import (
    Facility,
    Organization,
    Zone,
)
from apps.sensors.choices import SensorType
from apps.sensors.models import Sensor


User = get_user_model()


class DashboardOverviewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="dashboard_test",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_dashboard_overview_returns_200(self):
        url = reverse("dashboard-overview")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_dashboard_overview_contains_expected_sections(self):
        url = reverse("dashboard-overview")

        response = self.client.get(url)

        self.assertEqual(
            set(response.data.keys()),
            {
                "summary",
                "bins",
                "collections",
                "sensors",
                "recent_alerts",
            },
        )

    def test_dashboard_summary_contains_expected_fields(self):
        url = reverse("dashboard-overview")

        response = self.client.get(url)

        expected_fields = {
            "total_bins",
            "active_bins",
            "full_bins",
            "offline_bins",
            "average_fill_level",
            "total_sensors",
            "active_sensors",
            "active_alerts",
            "critical_alerts",
            "pending_collections",
            "completed_collections",
            "total_waste_collected_kg",
        }

        self.assertEqual(
            set(response.data["summary"].keys()),
            expected_fields,
        )

    def test_dashboard_requires_authentication(self):
        self.client.force_authenticate(user=None)

        url = reverse("dashboard-overview")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_dashboard_calculates_bin_statistics(self):
        organization = Organization.objects.create(
            name="Test Organization",
            code="TEST-ORG",
        )

        facility = Facility.objects.create(
            organization=organization,
            name="Test Facility",
            code="TEST-FAC",
        )

        zone = Zone.objects.create(
            facility=facility,
            name="Test Zone",
            code="TEST-ZONE",
        )

        SmartBin.objects.create(
            zone=zone,
            name="Bin 1",
            code="BIN-001",
            fill_level=20,
            status=BinStatus.LOW,
            is_active=True,
        )

        SmartBin.objects.create(
            zone=zone,
            name="Bin 2",
            code="BIN-002",
            fill_level=95,
            status=BinStatus.FULL,
            is_active=True,
        )

        SmartBin.objects.create(
            zone=zone,
            name="Bin 3",
            code="BIN-003",
            fill_level=0,
            status=BinStatus.OFFLINE,
            is_active=False,
        )

        url = reverse("dashboard-overview")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        summary = response.data["summary"]
        bins = response.data["bins"]

        self.assertEqual(
            summary["total_bins"],
            3,
        )

        self.assertEqual(
            summary["active_bins"],
            2,
        )

        self.assertEqual(
            summary["full_bins"],
            1,
        )

        self.assertEqual(
            summary["offline_bins"],
            1,
        )

        self.assertEqual(
            bins["total"],
            3,
        )

        self.assertEqual(
            bins["low"],
            1,
        )

        self.assertEqual(
            bins["full"],
            1,
        )

        self.assertEqual(
            bins["offline"],
            1,
        )

        self.assertEqual(
            summary["average_fill_level"],
            "38.33",
        )

    def test_dashboard_calculates_sensor_statistics(self):
        organization = Organization.objects.create(
            name="Sensor Organization",
            code="SENSOR-ORG",
        )

        facility = Facility.objects.create(
            organization=organization,
            name="Sensor Facility",
            code="SENSOR-FAC",
        )

        zone = Zone.objects.create(
            facility=facility,
            name="Sensor Zone",
            code="SENSOR-ZONE",
        )

        smart_bin = SmartBin.objects.create(
            zone=zone,
            name="Sensor Bin",
            code="SENSOR-BIN",
        )

        Sensor.objects.create(
            smart_bin=smart_bin,
            name="Ultrasonic Sensor",
            sensor_type=SensorType.ULTRASONIC,
            serial_number="SENSOR-001",
            is_active=True,
        )

        Sensor.objects.create(
            smart_bin=smart_bin,
            name="Weight Sensor",
            sensor_type=SensorType.WEIGHT,
            serial_number="SENSOR-002",
            is_active=True,
        )

        Sensor.objects.create(
            smart_bin=smart_bin,
            name="Temperature Sensor",
            sensor_type=SensorType.TEMPERATURE,
            serial_number="SENSOR-003",
            is_active=False,
        )

        url = reverse("dashboard-overview")

        response = self.client.get(url)

        sensors = response.data["sensors"]

        self.assertEqual(
            sensors["total"],
            3,
        )

        self.assertEqual(
            sensors["active"],
            2,
        )

        self.assertEqual(
            sensors["inactive"],
            1,
        )

        self.assertEqual(
            len(sensors["by_type"]),
            3,
        )

    def test_dashboard_calculates_alert_statistics(self):
        organization = Organization.objects.create(
            name="Alert Organization",
            code="ALERT-ORG",
        )

        facility = Facility.objects.create(
            organization=organization,
            name="Alert Facility",
            code="ALERT-FAC",
        )

        zone = Zone.objects.create(
            facility=facility,
            name="Alert Zone",
            code="ALERT-ZONE",
        )

        smart_bin = SmartBin.objects.create(
            zone=zone,
            name="Alert Bin",
            code="ALERT-BIN",
        )

        Alert.objects.create(
            smart_bin=smart_bin,
            alert_type=AlertType.BIN_FULL,
            title="Bin Full",
            message="The bin is full.",
            status=AlertStatus.ACTIVE,
            severity=AlertSeverity.HIGH,
        )

        Alert.objects.create(
            smart_bin=smart_bin,
            alert_type=AlertType.FIRE,
            title="Fire Detected",
            message="Fire detected near the bin.",
            status=AlertStatus.ACTIVE,
            severity=AlertSeverity.CRITICAL,
        )

        Alert.objects.create(
            smart_bin=smart_bin,
            alert_type=AlertType.BATTERY_LOW,
            title="Battery Low",
            message="Battery level is low.",
            status=AlertStatus.RESOLVED,
            severity=AlertSeverity.MEDIUM,
        )

        url = reverse("dashboard-overview")

        response = self.client.get(url)

        summary = response.data["summary"]

        self.assertEqual(
            summary["active_alerts"],
            2,
        )

        self.assertEqual(
            summary["critical_alerts"],
            1,
        )

    def test_dashboard_calculates_collection_statistics(self):
        organization = Organization.objects.create(
            name="Collection Organization",
            code="COLLECT-ORG",
        )

        facility = Facility.objects.create(
            organization=organization,
            name="Collection Facility",
            code="COLLECT-FAC",
        )

        zone = Zone.objects.create(
            facility=facility,
            name="Collection Zone",
            code="COLLECT-ZONE",
        )

        smart_bin = SmartBin.objects.create(
            zone=zone,
            name="Collection Bin",
            code="COLLECT-BIN",
        )

        route = CollectionRoute.objects.create(
            name="Route 1",
        )

        route.zones.add(zone)

        vehicle = CollectionVehicle.objects.create(
            registration_number="KAA 001A",
            name="Collection Truck",
            capacity_kg=5000,
        )

        driver = Driver.objects.create(
            first_name="Test",
            last_name="Driver",
            phone_number="0700000001",
            license_number="DL-001",
        )

        pending_schedule = CollectionSchedule.objects.create(
            route=route,
            vehicle=vehicle,
            driver=driver,
            scheduled_date=date.today(),
            scheduled_time=time(9, 0),
            status=ScheduleStatus.PENDING,
        )

        completed_schedule = CollectionSchedule.objects.create(
            route=route,
            vehicle=vehicle,
            driver=driver,
            scheduled_date=date.today(),
            scheduled_time=time(11, 0),
            status=ScheduleStatus.COMPLETED,
        )

        CollectionRecord.objects.create(
            schedule=completed_schedule,
            smart_bin=smart_bin,
            fill_level_before=90,
            weight_collected=120.50,
        )

        CollectionRecord.objects.create(
            schedule=completed_schedule,
            smart_bin=smart_bin,
            fill_level_before=80,
            weight_collected=79.50,
        )

        url = reverse("dashboard-overview")

        response = self.client.get(url)

        summary = response.data["summary"]
        collections = response.data["collections"]

        self.assertEqual(
            summary["pending_collections"],
            1,
        )

        self.assertEqual(
            summary["completed_collections"],
            1,
        )

        self.assertEqual(
            summary["total_waste_collected_kg"],
            "200.00",
        )

        self.assertEqual(
            collections["total_schedules"],
            2,
        )

        self.assertEqual(
            collections["pending"],
            1,
        )

        self.assertEqual(
            collections["completed"],
            1,
        )

        self.assertEqual(
            collections["total_waste_collected_kg"],
            "200.00",
        )

        self.assertEqual(
            collections["average_waste_collected_kg"],
            "100.00",
        )
