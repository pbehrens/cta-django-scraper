from django.db import models

from cta.scraper.models import Stop, Route 
# Create your models here.

class Trip(models.Model):
    station_id = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_station_id')
    stop_id = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_stop_id')
    station_name = models.CharField(max_length=200)
    stop_desc = models.CharField(max_length=200)
    run_number = models.IntegerField()
    route = models.ForeignKey(Route, to_field='route_short_name')
    destination = models.ForeignKey(Stop, to_field='stop_id', related_name='trip_destination')
    destination_name = models.CharField(max_length=150)
    route_direction_code = models.IntegerField()
    prediction_generated = models.DateTimeField()
    

    
#<?xml version="1.0" encoding="utf-8"?>
# <ctatt>
#<tmst>20120909 17:08:16</tmst>
#<errCd>0</errCd>
#<errNm />
# <eta>
#<staId>41320</staId>
#<stpId>30256</stpId>
#<staNm>Belmont</staNm>
#<stpDe>Service toward 95th/Dan Ryan</stpDe>
#<rn>817</rn>
#<rt>Red</rt>
#<destSt>0</destSt>
#<destNm>95th/Dan Ryan</destNm>
#<trDr>5</trDr>
#<prdt>20120909 17:05:38</prdt>
#<arrT>20120909 17:07:38</arrT>
#<isApp>0</isApp>
#<isSch>0</isSch>
#<isDly>0</isDly>
#<isFlt>0</isFlt>
#<flags />