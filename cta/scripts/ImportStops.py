csv_filepathname="/Users/thebeagle/dev/indstudy/cta/cta/fixtures/stops.txt"
# Full path to the directory immediately above your django project directory
project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"

# scrpae in data from  cta api
import sys,os
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

from cta.scraper.models import Stop

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
        
for row in dataReader:
    print row
    stop = Stop()
    stop.stop_id = int(row[0])
    if(row[1] != ''):
        stop.stop_code = int(row[1])
    else:
       stop.stop_code = None
    stop.stop_name = row[2]
    stop.stop_desc = row[3]
    stop.stop_lat = row[4]
    stop.stop_lon = row[5]
    stop.location_type = int(row[6])
    if row[7]:
        stop.parent_station = int(row[7])
    else:
        stop.parent_station = None
    stop.wheelchair_boarding = int(row[8])
    stop.save()