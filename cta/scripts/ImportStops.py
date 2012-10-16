############ All you need to modify is below ############
# Full path and name to your csv file
csv_filepathname="/Users/thebeagle/dev/indstudy/cta/cta/fixtures/stops.txt"
# Full path to the directory immediately above your django project directory
project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"

############ All you need to modify is above ############

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
#    if row[0]:
#        stop.stop_id = row[0]
#    else:
#        stop.stop_id = ''
#    if row[1]:
#        stop.stop_code = row[1]
#    else:
#        stop.stop_code = ''
#    if row[2]:
#        stop.stop_name = row[2]
#    else:
#        stop.stop_name = ''
#    if row[3]:
#        stop.stop_desc = row[3]
#    else:
#        stop.stop_desc = ''
#    if row[4]:
#        stop.stop_lat = row[4]
#    else:
#        stop.stop_lat = ''
#    if row[5]:
#        stop.stop_lon = row[5]
#    else:
#        stop.stop_lon = '' 
#    if row[6]:
#        stop.location_type = row[6]
#    else:
#        stop.location_type = ''
#        
#    if row[7]:
#        stop.parent_station = row[7]
#    else:
#        stop.parent_station = ''
#    if row[8]:
#        stop.wheelchair_boarding = row[8]
#    else:
#        stop.wheelchair_boarding = ''
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