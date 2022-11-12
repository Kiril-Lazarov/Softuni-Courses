from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin

from photo_gallery.accounts.models import AppUser

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    pass


'''
kqikkop7@wcss
'''