from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    """
    # list display shows displays of the users in admin panel
    list_display = ('username', "email", 'gender',
                    'language', 'currency', 'superhost')
    # list filter shows the filtering options for us (automatic from webframework)
    list_filter = ("currency", "language", "superhost",)
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )
    pass
