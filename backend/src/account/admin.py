from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUser, UserSettings

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
    ]


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(UserSettings)
