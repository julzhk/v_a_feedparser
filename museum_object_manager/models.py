from django.db import models
from museum_object_manager.museum_api import full_record_details

class MuseumRecord(models.Model):
    api_id = models.IntegerField(null=True)
    raw_data = models.TextField(blank=True)

    def __unicode__(self):
        return 'museum object:%s' % (self.api_id)

    def save(self):
        self.raw_data = full_record_details(id=self.api_id)
        super(MuseumRecord, self).save()
