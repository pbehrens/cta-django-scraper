#Script to retrieve data from the CTA API
#Will insert each ETA element into a trip object in the DB
 
# Full path to the directory immediately above your django project directory
project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"

import sys,os,urllib2, datetime
from Utils import get_tag_value

from xml.dom.minidom import parseString

#set up environment with django settings
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'
from django.db import models

from cta.trips.models import Trip 
from cta.scraper.models import Stop, Route, CtaTrip, Line
import datetime


#parse the xml you downloaded
#grab all of the line objects to be requested from the API
allLines = Line.objects.all()

# grab the eta elements and traverse through them
for stop in allLines:
    #create query string for the line object in question
    station_stop_id = stop.stop_id
    map_id = stop.parent_stop
    queryString = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=d2ca5e09289b40c2b54a826ddd822dba&mapid='+str(map_id)+'&max=6&stpid='+str(station_stop_id)
    
    #grab the xml file and convert to string:
    
    file = urllib2.urlopen(queryString)
    data = file.read()

    #close file because we dont need it anymore:
    file.close()
    dom = parseString(data)

    
    etaElements = dom.getElementsByTagName('eta')
    for eta in etaElements:
        # parse the relevant data from the xml response
        station_id = get_tag_value(eta.getElementsByTagName('staId')[0])
        stop_id = get_tag_value(eta.getElementsByTagName('stpId')[0])
        station_name = get_tag_value(eta.getElementsByTagName('staNm')[0])
        stop_desc = get_tag_value(eta.getElementsByTagName('stpDe')[0])
        run_number = get_tag_value(eta.getElementsByTagName('rn')[0])
        route = get_tag_value(eta.getElementsByTagName('rt')[0])
        destination = get_tag_value(eta.getElementsByTagName('destSt')[0])
        destination_name = get_tag_value(eta.getElementsByTagName('destNm')[0])
        route_direction_code = get_tag_value(eta.getElementsByTagName('trDr')[0])
        prediction_generated = get_tag_value(eta.getElementsByTagName('prdt')[0])
        expected_arrival = get_tag_value(eta.getElementsByTagName('arrT')[0])
        is_approaching = get_tag_value(eta.getElementsByTagName('isApp')[0])
        is_scheduled = get_tag_value(eta.getElementsByTagName('isSch')[0])
        is_delayed = get_tag_value(eta.getElementsByTagName('isDly')[0])
        is_fit = get_tag_value(eta.getElementsByTagName('isFlt')[0])
        
        #Make new trip object and populate with scraped data
        trip = Trip()
        stop = Stop.objects.get(parent_station=station_id, stop_id=stop_id)
        trip.station_id = stop
        trip.stop_id = stop
        
        db_route = Route.objects.get(route_id=route)
        trip.station_name = station_name
        trip.stop_desc = stop_desc
        trip.run_number = run_number
        trip.route = db_route
        trip.destination = stop
        trip.destination_name = destination_name
        trip.route_direction_code = route_direction_code
        #format datetime string to one that django can use
        prediction_generated = datetime.datetime.strptime(prediction_generated, '%Y%m%d %H:%M:%S')
        trip.prediction_generated = prediction_generated
        
        expected_arrival = datetime.datetime.strptime(expected_arrival, '%Y%m%d %H:%M:%S')
        trip.expected_arrival = expected_arrival
        trip.is_approaching = is_approaching
        trip.is_scheduled = is_scheduled
        trip.is_delayed = is_delayed
        trip.is_fit = is_fit
        trip.save()

