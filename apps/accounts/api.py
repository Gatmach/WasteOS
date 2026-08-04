from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.permissions import IsSuperAdmin
from apps.accounts.selectors import list_users
from apps.accounts.serializers import (
    ChangePasswordSerializer,
    LogoutSerializer,
    MeSerializer,
    UserCreateSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from apps.accounts.services import (
    change_password,
    create_user,
    update_user,
)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsSuperAdmin,
    )

    def get_queryset(self):
        return list_users()

    def get_permissions(self):
        if self.action in (
            "me",
            "change_password",
            "logout",
        ):
            permission_classes = (
                IsAuthenticated,
            )
        else:
            permission_classes = (
                IsAuthenticated,
                IsSuperAdmin,
            )

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return UserUpdateSerializer

        if self.action == "me":
            return MeSerializer

        return UserSerializer

    @action(
        detail=False,
        methods=["get"],
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.instance = create_user(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_user(
            serializer.instance,
            **serializer.validated_data,
        )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        change_password(
            request.user,
            serializer.validated_data["new_password"],
        )

        return Response(
            {"detail": "Password changed successfully."}
        )

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def logout(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Logged out successfully."}
        )