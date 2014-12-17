SearchMBTA
==========
This Python 2 project accesses real time data provided by the MBTA, accessible through their APIs. The data can be 
downloaded in XML or JSON format. This project experiments how data can be pulled from the site, and in what format. 

Documentation on APIs: 

Developer Portal: http://realtime.mbta.com/Portal/

Quick Start Guide: http://realtime.mbta.com/Portal/Content/Documents/MBTA-realtime_APIQuickStart_2014-08-04.pdf

Modules:
-------
get_mbta_230_bus_location.py: retrieves locations of the 230 bus that runs from Quincy Center -- near T.J.'s apartment -- to the Montello Commuter Rail -- near his old neighborhood.

The VehiclesByRoute query on the API retrieves:

Direction:
* direction_name: Whether the bus is Inbound or Outbound
* direction_id: 0 for outbound to Montello or 1: inbound to Quincy Center

Trip:
* trip_headsign: What the bus sign reads ("Montello via Braintree Station"). From this we can determine leg of the journey the bus is on, i.e. If it is leaving Quincy center and heading to Braintree Station, whether it has come from Braintree Station, whether it is going directly to the Montello Commuter Rail in Brockton, or if it is going on a side trip to the Linwood Housing project first. 
* trip_name: What time the bus left Quincy Center. 
* trip_id

Vehicle: 
* vehicle_timestamp 
* vehicle_lon: The longitude of the bus, according to GPS
* vehicle_lat: The latitude of the bus, according to GPS
* vehicle_id

get_MBTA_routes.py: retrieves all the routes the MBTA has operating. 



