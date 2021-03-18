from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.models import AbstractTableMeta


class lessons(AbstractTableMeta, models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    lecturer_name = models.CharField(max_length=100, default="", blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text="Enter number of hours")
    slides_url = models.CharField(max_length=255)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Attendance(AbstractTableMeta, models.Model):
    lessons = models.ForeignKey(lessons, on_delete=models.CASCADE)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
