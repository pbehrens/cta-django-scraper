project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
# Full path to the directory immediately above your django project directory
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"
csv_filepathname="/Users/thebeagle/dev/indstudy/cta/cta/fixtures/routes.txt"


import sys,os
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

from cta.scraper.models import Route

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
        
for row in dataReader:
    print row
    route = Route()
    route.route_id = row[0]
    if(row[1] != ''):
        route.route_short_name = row[1]
    else:
       route.route_short_name = None
   
    route.route_long_name = row[2]
    route.route_type = int(row[3])
    route.route_url = row[4]
    
    if row[5] != '':
        route.route_color = row[5]
    else:
       route.route_color = None
       
    if row[6] != '':
        route.route_color = row[6]
    else:
       route.route_color = None
          
    route.save()