from django.db import models

from apps.utils.models import Timestamps


class lessons(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    slides_url = models.CharField(max_length=255)
