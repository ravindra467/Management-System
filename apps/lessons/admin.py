from django.contrib import admin
from .models import lessons


class LessonsAdmin(admin.ModelAdmin):
    list_display = ("title", "lecturer_name", "date")
    search_fields = ("title", "lecturer_name")


admin.site.register(lessons, LessonsAdmin)