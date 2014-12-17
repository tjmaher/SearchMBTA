# get_MBTA_routes.py
#
#  This Python 2 program accesses real time data provided by the MBTA, accessible through 
#  their APIs. 
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
u = urllib.urlopen('http://realtime.mbta.com/developer/api/v2/routes?api_key=wX9NwuHnZU2ToO7GmGR9uw&format=xml')

data = u.read() # Get the XML Data retrieved and store it in the variable called 'data'.
f = open('MBTA_routes.xml', 'wb') # Open up a new file called "MBTA_route.xml", and set it to be a writable binary file. 
f.write(data)  # Write everything that was retrieved from the XML query and place it in the MBTA_routes.xml file. 
f.close()      # Close the file that was created. 
print('Wrote MBTA_routes.xml') # Output a message, if this program was run by the command line interface. 
