# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecordImage'
        db.create_table('museum_object_manager_recordimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museum_object_manager.MuseumRecord'])),
            ('src', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('museum_object_manager', ['RecordImage'])

        # Adding model 'MuseumRecord'
        db.create_table('museum_object_manager_museumrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('api_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('museum_object_manager', ['MuseumRecord'])


    def backwards(self, orm):
        # Deleting model 'RecordImage'
        db.delete_table('museum_object_manager_recordimage')

        # Deleting model 'MuseumRecord'
        db.delete_table('museum_object_manager_museumrecord')


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
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['museum_object_manager']