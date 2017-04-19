"""Test for api."""

from django.test import TestCase
import factory
from hikes.models import Hike
from django.urls import reverse_lazy
from django.test import Client, RequestFactory


class HikeFactory(factory.django.DjangoModelFactory):
    """Create hikes to test."""

    class Meta:
        """Invoke Hike instance."""

        model = Hike

    name = factory.Faker('word')
    date = factory.Faker('date')


class HikeFrontEndTests(TestCase):
    """Test hikes front end."""

    def setUp(self):
        """The setup and buildout for hikes."""
        self.client = Client()
        self.request = RequestFactory()
        self.hikes = [HikeFactory.create() for i in range(10)]

    def test_api_route_is_status_ok(self):
        """Funcional test for api."""
        response = self.client.get(reverse_lazy('api_list'))
        self.assertTrue(response.status_code == 200)

    def test_api_page_renders_correct_html(self):
        """Test authenticated user gets the right html on api."""
        hike = self.hikes[0]
        response = self.client.get(reverse_lazy('api_list'))
        self.assertTrue(hike.name.encode() in response.rendered_content)
