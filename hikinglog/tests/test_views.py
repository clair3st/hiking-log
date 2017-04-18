"""Test for front end."""

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

    def test_hike_add_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from hikes.views import CreateHike
        req = self.request.get(reverse_lazy("hike_add"))
        view = CreateHike.as_view()
        response = view(req)
        self.assertTrue(response.status_code == 200)

    def test_hike_add_route_is_status_ok(self):
        """Funcional test for add hike."""
        response = self.client.get(reverse_lazy("hike_add"))
        self.assertTrue(response.status_code == 200)

    def test_hike_add_route_uses_right_templates(self):
        """Test add hike returns the right templates."""
        response = self.client.get(reverse_lazy("hike_add"))
        self.assertTemplateUsed(response, "hikinglog/layout.html")
        self.assertTemplateUsed(response, "hikes/new_hike.html")

    def test_edit_hike_view_status_ok(self):
        """Rendered html has staus 200, Unit Test."""
        from hikes.views import EditHike
        req = self.request.get("/hikes/1/edit/")
        hike = self.hikes[0]
        view = EditHike.as_view()
        response = view(req, pk=hike.pk)
        self.assertTrue(response.status_code == 200)

    def test_edit_hike_route_is_status_ok(self):
        """Funcional test for edit hike."""
        hike = self.hikes[1]

        response = self.client.get(reverse_lazy(
            'edit_hike', kwargs={'pk': hike.id})
        )
        self.assertTrue(response.status_code == 200)

    def test_edit_hike_route_uses_right_templates(self):
        """Test edit hike returns the right templates."""
        hike = self.hikes[1]

        response = self.client.get(reverse_lazy(
            'edit_hike', kwargs={'pk': hike.id})
        )
        self.assertTemplateUsed(response, "hikinglog/layout.html")
        self.assertTemplateUsed(response, "hikes/edit_hike.html")
