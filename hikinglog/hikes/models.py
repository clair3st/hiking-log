"""Database models for hikes."""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Hike(models.Model):
    """Model for hike data."""

    name = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True)
    gain = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    duration = models.DurationField(null=True)
    distance = models.FloatField(null=True)
    region = models.CharField(max_length=255, blank=True)
    park = models.CharField(max_length=255, blank=True)
    weather = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        """String represntation of the model."""
        return self.title
