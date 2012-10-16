# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trip'
        db.create_table('trips_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trip_station_id', to_field='stop_id', to=orm['scraper.Stop'])),
            ('stop_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trip_stop_id', to_field='stop_id', to=orm['scraper.Stop'])),
            ('station_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('stop_desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('run_number', self.gf('django.db.models.fields.IntegerField')()),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scraper.Route'], to_field='route_short_name')),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trip_destination', to_field='stop_id', to=orm['scraper.Stop'])),
            ('destination_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('route_direction_code', self.gf('django.db.models.fields.IntegerField')()),
            ('prediction_generated', self.gf('django.db.models.fields.DateTimeField')()),
            ('expected_arrival', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_approaching', self.gf('django.db.models.fields.IntegerField')()),
            ('is_scheduled', self.gf('django.db.models.fields.IntegerField')()),
            ('is_fit', self.gf('django.db.models.fields.IntegerField')()),
            ('is_delayed', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('trips', ['Trip'])


    def backwards(self, orm):
        # Deleting model 'Trip'
        db.delete_table('trips_trip')


    models = {
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
        },
        'trips.trip': {
            'Meta': {'object_name': 'Trip'},
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_destination'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"}),
            'destination_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'expected_arrival': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approaching': ('django.db.models.fields.IntegerField', [], {}),
            'is_delayed': ('django.db.models.fields.IntegerField', [], {}),
            'is_fit': ('django.db.models.fields.IntegerField', [], {}),
            'is_scheduled': ('django.db.models.fields.IntegerField', [], {}),
            'prediction_generated': ('django.db.models.fields.DateTimeField', [], {}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraper.Route']", 'to_field': "'route_short_name'"}),
            'route_direction_code': ('django.db.models.fields.IntegerField', [], {}),
            'run_number': ('django.db.models.fields.IntegerField', [], {}),
            'station_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_station_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop_desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_stop_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"})
        }
    }

    complete_apps = ['trips']