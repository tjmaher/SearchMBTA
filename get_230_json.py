# get_MBTA_230_bus_location.py
#
#  This Python 2 program accesses real time data provided by the MBTA, accessible through 
#  their APIs. 
#
#  With this module we are searching for the "230: Quincy Center to Montello Station" bus line to see 
#  how many inbound and how many outbound buses are on the road at this moment travelling that route.
#
# The VehiclesByRoute query on the API retrieves:
# Direction:
# * direction_name: Whether the bus is Inbound or Outbound
# * direction_id: 0 for outbound to Montello in Brockton, MA or 1: inbound to Quincy Center in Quincy, MA
# 
# Trip:
# * trip_headsign: What the bus sign reads ("Montello via Braintree Station"). From this we can leg of the journey the bus 
# is on, i.e. Leaving Quincy center and heading to Braintree Station, whether it has come from Braintree Station, is going 
# directly to the Montello Commuter Rail in Brockton, or if it is going to the Linwood Housing project first. 
# * trip_name: What time the bus left Quincy Center. 
# * trip_id
# 
# Vehicle: 
# * vehicle_timestamp 
# * vehicle_lon: The longitude of the bus, according to GPS
# * vehicle_lat: The latitude of the bus, according to GPS
# * vehicle_id
#
#  MBTA's free API key is wX9NwuHnZU2ToO7GmGR9uw, given in 2013. They suggest if you are developing an app, 
#  that you apply for your own API Key.  
#
# Documentation of MBTA API's is at 
# http://realtime.mbta.com/Portal/Content/Documents/MBTA-realtime_APIDocumentation_v2_0_1_2014-09-08.pdf

# Open the query in a URL format, getting data on MBTA routes. The overall query format is:
# http://realtime.mbta.com/developer/api/v2/<query>?api_key=<your api key>
# &<parameter>=<required/optional parameters>

import urllib
u = urllib.urlopen('http://realtime.mbta.com/developer/api/v2/vehiclesbyroute?api_key=wX9NwuHnZU2ToO7GmGR9uw&route=230&format=json')

data = u.read() # Get the XML Data retrieved and store it in the variable called 'data'.
f = open('MBTA_230_buses.js', 'wb') # Open up a new file called "MBTA_230_bus_locations.xml", and set it to be a writable binary file. 
f.write(data)  # Write everything that was retrieved from the xml query and place it in the MBTA_230_bus_locations.xml file. 
f.close()      # Close the file that was created. 
print('Wrote MBTA_230_buses.js') # Output a message, if this program was run by the command line interface. 

