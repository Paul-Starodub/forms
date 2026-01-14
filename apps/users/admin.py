from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_editable = ("is_staff",)
    list_display_links = ("username",)
