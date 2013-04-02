from django.db import models
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib2
import requests
from PIL import Image
import os
from StringIO import StringIO

from museum_object_manager.museum_api import full_record_details
import json

IMAGE_EXTENSIONS = {
    'thumb':'_jpg_s',
    'small':'_jpg_o',
    'medium':'_jpg_ws',
    'mid':'_jpg_w',
    'large':'_jpg_ds',
    'bestfit':'_jpg_l',
    'max':'',
}

IMAGE_SIZES = (
    ('70px square crop','thumb'),
    ('130px square crop','small'),
    ('177px square crop','medium'),
    ('265px square crop','mid'),
    ('355px square fit','large'),
    ('768x600px best fit','bestfit'),
    ('768px (max) longest axis','max')
)
class RecordImage(models.Model):
    Record = models.ForeignKey('MuseumRecord')
    src = models.ImageField(upload_to='records')
    img_url = models.CharField(max_length=60,blank=True)
    img_size = models.CharField(max_length=20,choices=IMAGE_SIZES)

    def __unicode__(self):
        return 'museum img:%s (%s)' % (self.src, self.img_size)

    def save(self):
        super(RecordImage, self).save()
        if not self.src:
            r = requests.get(url=self.img_url)
            c = r.content
            fn = '%s-%s.jpg' %(self.Record.api_id, self.id)
            file_location = os.path.join(settings.MEDIA_ROOT,'records',fn)
            fileobject = open(file_location ,'wb')
            fileobject.write(c)
            fileobject.close()
            self.src = file_location
            self.save()


class MuseumRecord(models.Model):
    api_id = models.IntegerField(null=True)
    raw_data = models.TextField(blank=True)

    def __unicode__(self):
        return 'museum object:%s' % (self.api_id)

    def save(self):
        self.raw_data = json.dumps(full_record_details(id=self.api_id))
        super(MuseumRecord, self).save()
        # save an image for each size
        for imgsize in IMAGE_EXTENSIONS:
            r = RecordImage()
            r.Record = self
            r.img_size = imgsize
            r.img_url = self.get_image(imgsize)
            r.save()

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
        img_size = IMAGE_EXTENSIONS['max']
        return settings.MUSEUM_IMAGE_ROOT %(img_id[:6],img_id,img_size)


    def get_image(self,image_type):
        '''
        eg:

        http://media.vam.ac.uk/media/thira/collection_images/2007BL/2007BL8769.jpg
        '''
        img_id = self.get_primary_image_id
        if image_type in IMAGE_EXTENSIONS:
            img_size = IMAGE_EXTENSIONS[image_type]
        else:
            img_size = IMAGE_EXTENSIONS['small']
        return settings.MUSEUM_IMAGE_ROOT %(img_id[:6],img_id,img_size)
