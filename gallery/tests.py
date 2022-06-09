from  tests import TestCase
from .models import Category,Location
# Create your tests here.



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

