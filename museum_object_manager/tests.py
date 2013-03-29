"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from museum_api import keywordsearch, full_record_details
from models import MuseumRecord

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
        self.assertEquals(data['pk'],17079)
        self.assertEquals(data['fields']['artist'],'Rogers, William, Harry')


class Test_create_museum_object(TestCase):
    def test_create_object(self):
        testobject = MuseumRecord()
        testobject.api_id = 12345
        testobject.save()
        data = testobject.get_api_data
        self.assertEquals(data['fields']['artist'],'Rogers, William, Harry')

class Test_create_museum_object_that_has_img(TestCase):
    def test_create_object(self):
        testobject = MuseumRecord()
        testobject.api_id = 100554
        testobject.save()
        img_ref = testobject.get_primary_image_id
        self.assertEquals(img_ref, "2006AG6013")

class Test_get_img_url(TestCase):
    def test_create_object(self):
        testobject = MuseumRecord()
        testobject.api_id = 100554
        testobject.save()
        img_ref = testobject.get_primary_image_id
        self.assertEquals(
            testobject.get_primary_image,
            "http://media.vam.ac.uk/media/thira/collection_images/2006AG/2006AG6013.jpg"
        )

