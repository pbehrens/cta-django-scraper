csv_filepathname="/Users/thebeagle/dev/indstudy/cta/cta/fixtures/redline2.txt"
# Full path to the directory immediately above your django project directory
project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"

import sys,os
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

from cta.scraper.models import Line

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    print row
    line = Line()

    line.stop_id = int(row[0])
    if(row[1] != ''):
        line.direction = row[1]
    else:
       line.direction = None
    line.stop_name = row[2]
    line.stop_lat = row[3]
    line.stop_lon = row[4]
    line.station_name = row[5]
    line.station_description = row[6]
    if row[7]:
        line.parent_stop = row[7]
    else:
        line.parent_stop = None
    line.line = 'Red'
    line.save()