
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import IsSuperAdmin


class BaseAdminModelViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )