# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stop'
        db.create_table('scraper_stop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('stop_code', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('stop_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('stop_desc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('stop_lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8)),
            ('stop_lon', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8)),
            ('location_type', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('parent_station', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('wheelchair_boarding', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('scraper', ['Stop'])

        # Adding model 'Route'
        db.create_table('scraper_route', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_id', self.gf('django.db.models.fields.CharField')(max_length=8, unique=True, null=True)),
            ('route_short_name', self.gf('django.db.models.fields.CharField')(max_length=8, unique=True, null=True)),
            ('route_long_name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True)),
            ('route_type', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('route_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('route_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('route_text_color', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('scraper', ['Route'])

        # Adding model 'CtaTrip'
        db.create_table('scraper_ctatrip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('service_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('trip_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('direction_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('block_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('shape_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('wheelchair_accessible', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('scraper', ['CtaTrip'])

        # Adding model 'Line'
        db.create_table('scraper_line', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=8, unique=True, null=True)),
            ('stop_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('stop_lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8)),
            ('stop_lon', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=8)),
            ('station_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('station_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('parent_stop', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('scraper', ['Line'])


    def backwards(self, orm):
        # Deleting model 'Stop'
        db.delete_table('scraper_stop')

        # Deleting model 'Route'
        db.delete_table('scraper_route')

        # Deleting model 'CtaTrip'
        db.delete_table('scraper_ctatrip')

        # Deleting model 'Line'
        db.delete_table('scraper_line')


    models = {
        'scraper.ctatrip': {
            'Meta': {'object_name': 'CtaTrip'},
            'block_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'direction_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'service_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'shape_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'trip_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'wheelchair_accessible': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'scraper.line': {
            'Meta': {'object_name': 'Line'},
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '8', 'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'parent_stop': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'station_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'stop_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'stop_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'stop_lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'scraper.route': {
            'Meta': {'object_name': 'Route'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'unique': 'True', 'null': 'True'}),
            'route_long_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'}),
            'route_short_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'unique': 'True', 'null': 'True'}),
            'route_text_color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'route_type': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'route_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'scraper.stop': {
            'Meta': {'object_name': 'Stop'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'parent_station': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stop_code': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'stop_desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'stop_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'stop_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'stop_lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '8'}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'wheelchair_boarding': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['scraper']