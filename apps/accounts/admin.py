from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "organization",
        "facility",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
    )

    list_filter = (
        "role",
        "organization",
        "facility",
        "is_staff",
        "is_active",
    )

    autocomplete_fields = (
        "organization",
        "facility",
    )

    list_select_related = (
        "organization",
        "facility",
    )

    ordering = (
        "first_name",
        "last_name",
    )

    list_per_page = 25


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    autocomplete_fields = (
        "user",
    )

    list_per_page = 25