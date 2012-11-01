from django.db import models

# Create your models here.


class Prediction(models.Model):
    stop_id = models.IntegerField()
    stop_name = models.CharField(max_length=100, null=True)
    stop_desc = models.CharField(max_length=200, null=True)
    prediction_time = models.DateTimeField()
    is_delayed = models.IntegerField(default=0)
    location_type = models.CharField(max_length=150, null=True)
    parent_station = models.IntegerField()
    wheelchair_boarding = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.name

    def is_string(val):
        return False