"""Url for Hikes app."""


from django.conf.urls import url
from hikes.views import CreateHike, EditHike


urlpatterns = [
    url(r'^new/$', CreateHike.as_view(), name='hike_add'),
    url(r'^(?P<pk>\d+)/edit/$', EditHike.as_view(), name='edit_hike'),
]
