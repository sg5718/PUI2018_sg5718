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

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_sg5718.py apikey busname")
    sys.exit()
    
mtaurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,busname)
    
print (mtaurl)
response = urllib.urlopen(mtaurl)
data = response.read().decode("utf-8")
dataDict = json.loads(data)


Allbuses = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

outputdata = open(sys.argv[3],'w')
outputdata.write('Latitude,Longitude,Stop Name,Stop Status\n')

for i in range(len(Allbuses)):
    latitude = Allbuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = Allbuses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try:
        stopinformation = Allbuses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
        stopname = stopinformation['StopPointName']
        stopstatus = stopinformation['Extensions']['Distances']['PresentableDistance']   
    except LookupError:
        stopname = stopstatus = 'N/A'        
    outputdata.write('%s,%s,%s,%s\n'%(latitude,longitude,stopname,stopstatus))
outputdata.close()

