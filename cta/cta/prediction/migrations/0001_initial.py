# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prediction'
        db.create_table('prediction_prediction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_id', self.gf('django.db.models.fields.IntegerField')()),
            ('stop_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('stop_desc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('prediction_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_delayed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location_type', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('parent_station', self.gf('django.db.models.fields.IntegerField')()),
            ('wheelchair_boarding', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('prediction', ['Prediction'])


    def backwards(self, orm):
        # Deleting model 'Prediction'
        db.delete_table('prediction_prediction')


    models = {
        'prediction.prediction': {
            'Meta': {'object_name': 'Prediction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delayed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'location_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'parent_station': ('django.db.models.fields.IntegerField', [], {}),
            'prediction_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'stop_id': ('django.db.models.fields.IntegerField', [], {}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'wheelchair_boarding': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['prediction']