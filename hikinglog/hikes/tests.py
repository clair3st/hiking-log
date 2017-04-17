"""Test hike models and views."""

from django.test import TestCase
import factory
from hikes.models import Hike
import datetime


class HikeFactory(factory.django.DjangoModelFactory):
    """Create hikes to test."""

    class Meta:
        """Invoke Hike instance."""

        model = Hike

    name = factory.Faker('word')
    date = factory.Faker('date')


class HikeTestCase(TestCase):
    """Test hikes."""

    def setUp(self):
        """The setup and buildout for hikes."""
        self.hikes = [HikeFactory.create() for i in range(10)]

    def test_hike_creation(self):
        """Test the created name is the same as the expected name."""
        w = self.hikes[0]
        self.assertIsInstance(w, Hike)
        self.assertEqual(w.__str__(), w.name)

    def test_hike_date(self):
        """Test the Hike is created with a date."""
        hike = self.hikes[0]
        date = datetime.datetime.strptime(hike.date, '%Y-%m-%d')
        self.assertIsInstance(date, datetime.datetime)

    def test_hike_has_attributes(self):
        """Test hike is created with attributes."""
        hike = self.hikes[0]
        attributes = ['name',
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
        for attribute in attributes:
            self.assertTrue(hasattr(hike, attribute))

    def test_set_gain_not_a_number(self):
        """Assert gain can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.gain, 'not a number')

    def test_set_gain_a_number(self):
        """Test gain can be set with a number."""
        hike = self.hikes[0]
        hike.gain = 2000
        self.assertTrue(hike.gain is 2000)

    def test_set_height_a_number(self):
        """Test height can be set with a number."""
        hike = self.hikes[0]
        hike.height = 2000
        self.assertTrue(hike.height is 2000)

    def test_set_height_not_a_number(self):
        """Assert height can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.height, 'not a number')

    def test_set_distance_a_number(self):
        """Test distance can be set with a number."""
        hike = self.hikes[0]
        hike.distance = 2000
        self.assertTrue(hike.distance is 2000)

    def test_set_distance_not_a_number(self):
        """Assert distance can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.distance, 'not a number')

    def test_set_duration_a_number(self):
        """Test duration can be set with a number."""
        hike = self.hikes[0]
        hike.duration = 2000
        self.assertTrue(hike.duration is 2000)

    def test_set_duration_not_a_number(self):
        """Assert duration can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.duration, 'not a number')

    def test_set_lat(self):
        """Test set lat."""
        self.hikes[2].lat = 47.6062
        self.assertTrue(self.hikes[2].lat is 47.6062)

    def test_set_lat_not_a_number(self):
        """Assert lat can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.lat, 'not a number')

    def test_set_lng(self):
        """Test set lng."""
        self.hikes[2].lng = 47.6062
        self.assertTrue(self.hikes[2].lng is 47.6062)

    def test_set_lng_not_a_number(self):
        """Assert lng can't be set as a string."""
        hike = self.hikes[0]
        self.assertRaises(ValueError, hike.lng, 'not a number')
