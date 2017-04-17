"""Test hike models and views."""

from django.test import TestCase
import factory
from hikes.models import Hike


class HikeFactory(factory.django.DjangoModelFactory):
    """Create hikes to test."""

    class Meta:
        """Invoke Hike instance."""

        model = Hike

    name = factory.Faker('title')


class HikeTestCase(TestCase):
    """Test hikes."""

    def setUp(self):
        """The setup and buildout for hikes."""
        self.hikes = [HikeFactory.create() for i in range(10)]
