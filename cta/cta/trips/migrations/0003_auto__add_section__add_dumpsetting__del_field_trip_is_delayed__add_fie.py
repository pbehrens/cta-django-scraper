# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table('trips_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section_start_id', to_field='stop_id', to=orm['scraper.Stop'])),
            ('end_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='section_end_id', to_field='stop_id', to=orm['scraper.Stop'])),
            ('run_number', self.gf('django.db.models.fields.IntegerField')()),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('trips', ['Section'])

        # Adding model 'DumpSetting'
        db.create_table('trips_dumpsetting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_retrieved', self.gf('django.db.models.fields.IntegerField')()),
            ('time_retrieved', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('trips', ['DumpSetting'])

        # Deleting field 'Trip.is_delayed'
        db.delete_column('trips_trip', 'is_delayed')

        # Adding field 'Trip.degree'
        db.add_column('trips_trip', 'degree',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table('trips_section')

        # Deleting model 'DumpSetting'
        db.delete_table('trips_dumpsetting')

        # Adding field 'Trip.is_delayed'
        db.add_column('trips_trip', 'is_delayed',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Trip.degree'
        db.delete_column('trips_trip', 'degree')


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
        'trips.dumpsetting': {
            'Meta': {'object_name': 'DumpSetting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_retrieved': ('django.db.models.fields.IntegerField', [], {}),
            'time_retrieved': ('django.db.models.fields.DateTimeField', [], {})
        },
        'trips.section': {
            'Meta': {'object_name': 'Section'},
            'end_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section_end_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'run_number': ('django.db.models.fields.IntegerField', [], {}),
            'start_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'section_start_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"})
        },
        'trips.trip': {
            'Meta': {'object_name': 'Trip'},
            'degree': ('django.db.models.fields.IntegerField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_destination'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"}),
            'destination_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'expected_arrival': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approaching': ('django.db.models.fields.IntegerField', [], {}),
            'is_fit': ('django.db.models.fields.IntegerField', [], {}),
            'is_scheduled': ('django.db.models.fields.IntegerField', [], {}),
            'prediction_generated': ('django.db.models.fields.DateTimeField', [], {}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scraper.Route']", 'to_field': "'route_id'"}),
            'route_direction_code': ('django.db.models.fields.IntegerField', [], {}),
            'run_number': ('django.db.models.fields.IntegerField', [], {}),
            'station_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_station_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"}),
            'station_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop_desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trip_stop_id'", 'to_field': "'stop_id'", 'to': "orm['scraper.Stop']"})
        }
    }

    complete_apps = ['trips']