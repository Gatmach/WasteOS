from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User
from apps.organizations.models import Organization

from .choices import ReportStatus, ReportType
from .models import Report
from .services import (
    create_report,
    delete_report,
    mark_report_completed,
    mark_report_failed,
    mark_report_processing,
)
from .selectors import (
    get_facility_reports,
    get_organization_reports,
    get_report,
    get_reports,
    get_reports_by_status,
    get_reports_by_type,
    get_recent_reports,
    get_user_reports,
)


class ReportServiceTests(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(
            name="Test Organization",
            code="TEST-ORG",
        )

        self.user = User.objects.create_user(
            username="reportuser",
            email="report@example.com",
            password="StrongPassword123!",
            phone_number="+254700000001",
            organization=self.organization,
        )

    def test_create_report(self):
        report = create_report(
            name="Collection Report",
            report_type=ReportType.COLLECTION,
            generated_by=self.user,
        )

        self.assertEqual(report.name, "Collection Report")
        self.assertEqual(
            report.report_type,
            ReportType.COLLECTION,
        )
        self.assertEqual(
            report.status,
            ReportStatus.PENDING,
        )
        self.assertEqual(
            report.generated_by,
            self.user,
        )

    def test_mark_report_processing(self):
        report = create_report(
            name="Bin Report",
            report_type=ReportType.BIN,
            generated_by=self.user,
        )

        mark_report_processing(report)

        report.refresh_from_db()

        self.assertEqual(
            report.status,
            ReportStatus.PROCESSING,
        )

    def test_mark_report_completed(self):
        report = create_report(
            name="Analytics Report",
            report_type=ReportType.ANALYTICS,
            generated_by=self.user,
        )

        mark_report_completed(report)

        report.refresh_from_db()

        self.assertEqual(
            report.status,
            ReportStatus.COMPLETED,
        )
        self.assertIsNotNone(report.generated_at)

    def test_mark_report_failed(self):
        report = create_report(
            name="Sensor Report",
            report_type=ReportType.SENSOR,
            generated_by=self.user,
        )

        mark_report_failed(report)

        report.refresh_from_db()

        self.assertEqual(
            report.status,
            ReportStatus.FAILED,
        )

    def test_delete_report_soft_deletes(self):
        report = create_report(
            name="Alert Report",
            report_type=ReportType.ALERT,
            generated_by=self.user,
        )

        delete_report(report)

        report.refresh_from_db()

        self.assertTrue(report.is_deleted)

        self.assertEqual(
            get_reports().count(),
            0,
        )


class ReportSelectorTests(TestCase):

    def setUp(self):
        self.organization = Organization.objects.create(
            name="Selector Organization",
            code="SEL-ORG",
        )

        self.user = User.objects.create_user(
            username="selectoruser",
            email="selector@example.com",
            password="StrongPassword123!",
            phone_number="+254700000002",
            organization=self.organization,
        )

        self.report = Report.objects.create(
            name="Collection Report",
            report_type=ReportType.COLLECTION,
            generated_by=self.user,
            status=ReportStatus.COMPLETED,
        )

    def test_get_reports(self):
        reports = get_reports()

        self.assertEqual(reports.count(), 1)
        self.assertEqual(reports.first(), self.report)

    def test_get_report(self):
        report = get_report(self.report.id)

        self.assertEqual(report, self.report)

    def test_get_user_reports(self):
        reports = get_user_reports(self.user)

        self.assertEqual(reports.count(), 1)
        self.assertEqual(reports.first(), self.report)

    def test_get_organization_reports(self):
        reports = get_organization_reports(self.user)

        self.assertEqual(reports.count(), 1)

    def test_get_reports_by_type(self):
        reports = get_reports_by_type(
            ReportType.COLLECTION
        )

        self.assertEqual(reports.count(), 1)

    def test_get_reports_by_status(self):
        reports = get_reports_by_status(
            ReportStatus.COMPLETED
        )

        self.assertEqual(reports.count(), 1)

    def test_get_recent_reports(self):
        reports = get_recent_reports(limit=5)

        self.assertEqual(reports.count(), 1)

class ReportAPITests(APITestCase):

    def setUp(self):
        self.organization = Organization.objects.create(
            name="API Organization",
            code="API-ORG",
        )

        self.user = User.objects.create_user(
            username="apiuser",
            email="api@example.com",
            password="StrongPassword123!",
            phone_number="+254700000003",
            organization=self.organization,
        )

        self.client.force_authenticate(user=self.user)

    def test_list_reports(self):
        Report.objects.create(
            name="Collection Report",
            report_type=ReportType.COLLECTION,
            generated_by=self.user,
        )

        url = reverse("report-list-create")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_report(self):
        url = reverse("report-list-create")

        response = self.client.post(
            url,
            {
                "name": "Analytics Report",
                "report_type": ReportType.ANALYTICS,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["name"],
            "Analytics Report",
        )

        self.assertEqual(
            response.data["report_type"],
            ReportType.ANALYTICS,
        )

        self.assertEqual(
            response.data["status"],
            ReportStatus.PENDING,
        )

        self.assertEqual(
            response.data["generated_by"],
            self.user.id,
        )
    def test_created_report_belongs_to_authenticated_user(self):
        url = reverse("report-list-create")

        response = self.client.post(
            url,
            {
                "name": "Security Report",
                "report_type": ReportType.ALERT,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        report = Report.objects.get(
            id=response.data["id"]
        )

        self.assertEqual(
            report.generated_by,
            self.user,
        )

    def test_retrieve_report(self):
        report = Report.objects.create(
            name="Bin Report",
            report_type=ReportType.BIN,
            generated_by=self.user,
        )

        url = reverse(
            "report-detail",
            kwargs={"report_id": report.id},
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["id"],
            str(report.id),
        )

    def test_unauthenticated_user_cannot_list_reports(self):
        self.client.force_authenticate(user=None)

        url = reverse("report-list-create")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_unauthenticated_user_cannot_create_report(self):
        self.client.force_authenticate(user=None)

        url = reverse("report-list-create")

        response = self.client.post(
            url,
            {
                "name": "Unauthorized Report",
                "report_type": ReportType.BIN,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )
    
    def test_user_cannot_retrieve_another_users_report(self):
        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="StrongPassword123!",
            phone_number="+254700000004",
            organization=self.organization,
        )

        report = Report.objects.create(
            name="Private Report",
            report_type=ReportType.ANALYTICS,
            generated_by=other_user,
        )

        url = reverse(
            "report-detail",
            kwargs={"report_id": report.id},
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_list_reports_only_returns_authenticated_users_reports(self):
        other_user = User.objects.create_user(
            username="otheruser2",
            email="other2@example.com",
            password="StrongPassword123!",
            phone_number="+254700000005",
            organization=self.organization,
        )

        Report.objects.create(
            name="My Report",
            report_type=ReportType.BIN,
            generated_by=self.user,
        )

        Report.objects.create(
            name="Other User Report",
            report_type=ReportType.ALERT,
            generated_by=other_user,
        )

        url = reverse("report-list-create")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["name"],
            "My Report",
        )