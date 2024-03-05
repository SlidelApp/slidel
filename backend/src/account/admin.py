from django.contrib import admin  # noqa

# Register your models here.

from django.contrib import admin
from .models import UserSettings

# Register your models here.
admin.site.register(UserSettings)