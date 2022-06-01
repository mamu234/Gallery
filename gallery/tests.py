from django.test import TestCase

# Create your tests here.
from .models import Category,Location


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category=Category(name = 'food')

def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.location=Location(name = 'Afirca')

def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

