# get_MBTA_routes.py
#
# Access the MBTA website and fetch information
# about all route the MBTA has.  Write to a file 'MBTA_Routes.xml'.

# MBTA's free API key is wX9NwuHnZU2ToO7GmGR9uw
#
# Documentation of MBTA API's is at 
# http://realtime.mbta.com/Portal/Content/Documents/MBTA-realtime_APIDocumentation_v2_0_1_2014-09-08.pdf

import urllib
u = urllib.urlopen('http://realtime.mbta.com/developer/api/v2/routes?api_key=wX9NwuHnZU2ToO7GmGR9uw&format=xml')

data = u.read()
f = open('MBTA_routes.xml', 'wb')
f.write(data)
f.close()
print('Wrote MBTA_routes.xml')
