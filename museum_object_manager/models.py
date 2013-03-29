from django.db import models

class MuseumRecord(models.Model):
    api_id = models.IntegerField(null=True)
    raw_data = models.TextField(null=True)

    def __unicode__(self):
        return 'museum object:%s' % (self.api_id)

