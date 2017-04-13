"""Api."""

from django.conf.urls import url
from hike_api.views import HikeViewSet

urlpatterns = [
    # url(r'^hikes/(?P<pk>[0-9]+)/$', views.hike_detail),
    url(r'^hikes/$', HikeViewSet.as_view({'get': 'list'}), name='api_list')
]
