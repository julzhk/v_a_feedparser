from django.db import models

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