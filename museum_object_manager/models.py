from django.db import models
from django.conf import settings

from museum_object_manager.museum_api import full_record_details
import json

class MuseumRecord(models.Model):
    api_id = models.IntegerField(null=True)
    raw_data = models.TextField(blank=True)

    def __unicode__(self):
        return 'museum object:%s' % (self.api_id)

    def save(self):
        self.raw_data = json.dumps(full_record_details(id=self.api_id))
        super(MuseumRecord, self).save()

    @property
    def get_api_data(self):
        return json.loads(self.raw_data)

    def get_field(self, fieldname):
        return self.get_api_data['fields'][fieldname]

    @property
    def get_primary_image_id(self):
        '''
        convenience method to just pull out the primary_image_id
        '''
        return self.get_field('primary_image_id')

    @property
    def get_primary_image(self):
        '''
        eg:

        http://media.vam.ac.uk/media/thira/collection_images/2007BL/2007BL8769.jpg
        '''
        img_id = self.get_primary_image_id
        return settings.MUSEUM_IMAGE_ROOT %(img_id[:6],img_id)
