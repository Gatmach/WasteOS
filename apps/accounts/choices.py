
from django.db import models

class UserRole(models.TextChoices):
    SUPER_ADMIN = "super_admin", "Super Admin"
    ORGANIZATION_ADMIN = "organization_admin", "Organization Admin"
    FACILITY_MANAGER = "facility_manager", "Facility Manager"
    SUPERVISOR = "supervisor", "Supervisor"
    OPERATOR = "operator", "Operator"
    DRIVER = "driver", "Driver"
    TECHNICIAN = "technician", "Technician"
    VIEWER = "viewer", "Viewer"