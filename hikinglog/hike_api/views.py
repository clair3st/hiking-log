"""View API endpoint."""

from rest_framework import viewsets
from hikes.models import Hike
from hike_api.serializers import HikeSerializer
# from django.urls import reverse_lazy


class HikeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
