from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accounts.services import create_user
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "full_name",
            "role",
            "organization",
            "facility",
            "is_active",
            "is_staff",
            "date_joined",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "is_active",
            "is_staff",
            "date_joined",
            "created_at",
            "updated_at",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "password",
            "first_name",
            "last_name",
            "role",
            "organization",
            "facility",
        )

    def create(self, validated_data):
        return create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "role",
            "organization",
            "facility",
        )


class MeSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "full_name",
            "role",
            "organization",
            "facility",
        )

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        write_only=True,
        required=True,
    )

    new_password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
    )

    def validate_old_password(self, value):
        user = self.context["request"].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                "Old password is incorrect."
            )

        return value

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        token = RefreshToken(self.validated_data["refresh"])
        token.blacklist()