# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RecordImage.img_url'
        db.add_column('museum_object_manager_recordimage', 'img_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RecordImage.img_url'
        db.delete_column('museum_object_manager_recordimage', 'img_url')


    models = {
        'museum_object_manager.museumrecord': {
            'Meta': {'object_name': 'MuseumRecord'},
            'api_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'museum_object_manager.recordimage': {
            'Meta': {'object_name': 'RecordImage'},
            'Record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['museum_object_manager.MuseumRecord']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_size': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'img_url': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['museum_object_manager']