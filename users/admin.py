from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "last_name", "first_name", "is_active", "last_login")
    search_fields = ("email", "last_name")
