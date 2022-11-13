from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin

from photo_gallery.accounts.models import AppUser

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "gender"
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


'''
kqikkop7@wcss
'''