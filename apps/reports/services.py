
from django.utils import timezone

from apps.accounts.models import User

from .choices import ReportStatus
from .models import Report


def create_report(
    *,
    name: str,
    report_type: str,
    generated_by: User,
) -> Report:
    """
    Create a new report in PENDING state.
    """
    return Report.objects.create(
        name=name,
        report_type=report_type,
        generated_by=generated_by,
        status=ReportStatus.PENDING,
    )


def mark_report_processing(
    report: Report,
) -> Report:
    """
    Mark a report as currently being generated.
    """
    report.status = ReportStatus.PROCESSING

    report.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return report


def mark_report_completed(
    report: Report,
) -> Report:
    """
    Mark a report as successfully generated.
    """
    report.status = ReportStatus.COMPLETED
    report.generated_at = timezone.now()

    report.save(
        update_fields=[
            "status",
            "generated_at",
            "updated_at",
        ]
    )

    return report


def mark_report_failed(
    report: Report,
) -> Report:
    """
    Mark a report as failed.
    """
    report.status = ReportStatus.FAILED

    report.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return report


def delete_report(
    report: Report,
) -> Report:
    """
    Soft-delete a report.
    """
    report.is_deleted = True

    report.save(
        update_fields=[
            "is_deleted",
            "updated_at",
        ]
    )

    return report