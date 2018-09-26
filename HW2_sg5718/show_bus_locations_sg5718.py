# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

apikey = sys.argv[1]
busname = sys.argv[2]

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_sg5718.py apikey busname")
    sys.exit()
    
mtaurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busname)
    
print (mtaurl)
response = urllib.urlopen(mtaurl)
data = response.read().decode("utf-8")
dataDict = json.loads(data)


Allbuses = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print('Bus Line: %s'%(busname))
print('Number of Active Buses : %s'%(len(Allbuses)))

for i in range(0,len(Allbuses)):
    latitude = Allbuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = Allbuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print('Bus %s is at latitude %s and longitude %s'%(i,latitude,longitude))
