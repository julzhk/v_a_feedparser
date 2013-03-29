# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RecordImage.img_size'
        db.add_column('museum_object_manager_recordimage', 'img_size',
                      self.gf('django.db.models.fields.CharField')(default='thumb', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RecordImage.img_size'
        db.delete_column('museum_object_manager_recordimage', 'img_size')


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
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['museum_object_manager']