"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from museum_api import keywordsearch, full_record_details

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_museum_api(self):
        data = keywordsearch(term='wooden_door')
        self.assertTrue(isinstance(data, list))


    def test_full_record_details(self):
        data = full_record_details('12345')
        self.assertEquals(data[0]['pk'],17079)
