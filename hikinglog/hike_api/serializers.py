"""Serializing and deserializing the photo instances into json."""

from rest_framework import serializers
from hikes.models import Hike


class HikeSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize Hike model data."""

    class Meta:
        """Hike model and fields."""

        model = Hike
        fields = ['name',
                  'date',
                  'gain',
                  'height',
                  'duration',
                  'distance',
                  'region',
                  'park',
                  'lat',
                  'lng']
