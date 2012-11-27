project_folder="/Users/thebeagle/dev/indstudy/cta/cta"

project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"
csv_filepathname="/Users/thebeagle/dev/indstudy/cta/cta/fixtures/trips.txt"


import sys,os
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

from cta.scraper.models import CtaTrip
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
firstrow = True      
for row in dataReader:
    if firstrow != True:
        print row
        cta_trip = CtaTrip()
        cta_trip.route_id = row[0]
        cta_trip.service_id = row[1]
        cta_trip.trip_id = row[2]
        cta_trip.direction_id = int(row[3])
        cta_trip.block_id = row[4]
        cta_trip.shape_id = row[5]
        cta_trip.direction = row[6]
        cta_trip.wheelchair_accessible = row[7]
        cta_trip.save()
    firstrow = False