"""View API endpoint."""

from rest_framework import viewsets
from imager_images.models import Hike
from imager_api.serializers import HikeSerializer
# from django.urls import reverse_lazy


class HikeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
