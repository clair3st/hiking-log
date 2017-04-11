"""View Class for hiking app."""

from hikes.models import Hikes
from django.views.generic import (CreateView,
                                  UpdateView)
from django.urls import reverse_lazy


class CreateHike(CreateView):
    """Add a hike."""

    template_name = 'hikes/new_hike.html'
    model = Hikes
    fields = ['name',
              'date',
              'gain',
              'height',
              'duration',
              'distance',
              'region',
              'park',
              'weather',
              'notes',
              'lat',
              'lng']
    success_url = reverse_lazy("home")


class EditHike(UpdateView):
    """Edit a hike."""

    template_name = "hikes/edit_hike.html"
    success_url = reverse_lazy("home")
    model = Hikes
    fields = ['name',
              'date',
              'gain',
              'height',
              'duration',
              'distance',
              'region',
              'park',
              'weather',
              'notes',
              'lat',
              'lng']
