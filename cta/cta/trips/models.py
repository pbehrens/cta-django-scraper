from django.db import models

from cta.scraper.models import Stop, Route 
# Create your models here.

class Trip(models.Model):
    station_id = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_station_id')
    stop_id = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_stop_id')
    station_name = models.CharField(max_length=200)
    stop_desc = models.CharField(max_length=200)
    run_number = models.IntegerField()
    route = models.ForeignKey(Route, to_field='route_id')
    destination = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_destination')
    destination_name = models.CharField(max_length=150)
    route_direction_code = models.IntegerField()
    prediction_generated = models.DateTimeField()
    expected_arrival = models.DateTimeField()
    is_approaching = models.IntegerField()
    is_scheduled = models.IntegerField()
    is_fit = models.IntegerField()
    is_delayed = models.IntegerField()
    degree = models.IntegerField()
    time_scraped = models.DateTimeField()
    

class Section(models.Model):
	start_id = models.ForeignKey(Stop, to_field='stop_id', related_name='section_start_id')
	end_id = models.ForeignKey(Stop, to_field='stop_id', related_name='section_end_id')
	run_number = models.IntegerField()
	line = models.CharField(max_length=200)
	
class DumpSetting(models.Model):
	last_retrieved = models.IntegerField()
	time_retrieved = models.DateTimeField()
	
	
