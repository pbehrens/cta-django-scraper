#Script to retrieve data from the CTA API
#Will insert each ETA element into a trip object in the DB
 
# Full path to the directory immediately above your django project directory
project_folder="/Users/thebeagle/dev/indstudy/cta/cta"
project_parent="/Users/thebeagle/dev/indstudy/cta/cta/cta"

import sys,os,urllib2

from xml.dom.minidom import parseString

#set up environment with django settings
sys.path.append(project_folder)
sys.path.append(project_parent)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

from cta.trips.models import Trip 

#download the file:
file = urllib2.urlopen('http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=d2ca5e09289b40c2b54a826ddd822dba&mapid=41320&max=6&stpid=30256')
#convert to string:
data = file.read()

#close file because we dont need it anymore:
file.close()

print(data)







##parse the xml you downloaded
#dom = parseString(data)
##retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
#xmlTag = dom.getElementsByTagName('tagName')[0].toxml()
##strip off the tag (<tag>data</tag>  --->   data):
#xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
##print out the xml tag and data in this format: <tag>data</tag>
#print xmlTag
##just print the data
#print xmlData
#
#datetime.strptime(parsed_date, '%Y%m%d %H:%M:%S')
