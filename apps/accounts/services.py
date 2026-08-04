from django.db import transaction

from apps.accounts.models import User


@transaction.atomic
def create_user(**validated_data) -> User:
    password = validated_data.pop("password")

    user = User(**validated_data)
    user.set_password(password)
    user.save()

    return user


@transaction.atomic
def update_user(
    user: User,
    **validated_data,
) -> User:
    password = validated_data.pop("password", None)

    for field, value in validated_data.items():
        setattr(user, field, value)

    if password:
        user.set_password(password)

    user.save()

    return user


@transaction.atomic
def change_password(
    user: User,
    password: str,
) -> User:
    user.set_password(password)
    user.save(update_fields=["password"])

    return user


@transaction.atomic
def activate_user(user: User) -> User:
    user.is_active = True
    user.save(update_fields=["is_active"])

    return user


@transaction.atomic
def deactivate_user(user: User) -> User:
    user.is_active = False
    user.save(update_fields=["is_active"])

    return user