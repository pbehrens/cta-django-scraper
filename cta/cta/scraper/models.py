from django.db import models

# Create your models here.


class Stop(models.Model):
    stop_id = models.IntegerField(null=True, unique=True)
    stop_code = models.IntegerField(null=True, unique=True)
    stop_name = models.CharField(max_length=100, null=True)
    stop_desc = models.CharField(max_length=200, null=True)
    stop_lat = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    stop_lon = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    location_type = models.CharField(max_length=150, null=True)
    parent_station =  models.IntegerField(null=True)
    wheelchair_boarding = models.IntegerField(null=True)

class Route(models.Model):
    route_id = models.CharField(max_length=8, null=True, unique=True)
    route_short_name = models.CharField(max_length=8, null=True, unique=True)
    route_long_name = models.CharField(max_length=100, null=True, unique=True)
    route_type = models.IntegerField(null=True)
    route_url = models.CharField(max_length=200, null=True)
    route_color = models.CharField(max_length=50, null=True)
    route_text_color = models.CharField(max_length=50, null=True)
    