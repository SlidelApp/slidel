from django.contrib import admin
from .models import Slides
# Register your models here.
class SlidesAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "user"]
    search_fields = ["title"]
    list_filter = ["user"]
    list_per_page = 20

admin.site.register(Slides, SlidesAdmin)
admin.site.register(Slides)
