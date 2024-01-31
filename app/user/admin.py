"""
Define admin classes for managing models in the Django admin interface.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user import models


class UserAdmin(BaseUserAdmin):
    """
    Custom UserAdmin class to define the admin pages for managing user models.

    This class extends the Django BaseUserAdmin class to customize the admin interface
    for the User model.
    """

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "dob",
                    "created_at",
                    "modified_at",
                )
            },
        ),
    )
    readonly_fields = [
        "created_at",
        "modified_at",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
