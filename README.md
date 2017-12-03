# citybikes-mqtt.py
Look up CityBikes station and publish information to MQTT.

Find your network
https://api.citybik.es/v2/

Go to the network endpoint ie.
https://api.citybik.es/v2/ford-gobike

Search for that station, note IDs.

Add IDs to myStations list:
```
myStations = ["8302e5d11a6c84bac27a774de41474f9", \
               "c2648d0ffed4d1f710ccaf79e9a304fa", \
               "3f5c0437929a0f6dbc32f116850a4196", \
               "36aa8ab83177d5f5beb83685c7f645d3"]
```

# MQTT Output
```
CityBikes/Frank H Ogawa Plaza {"last_updated": "2017-12-03 09:19", "lon": -122.27173805236816, "percent_full": 31, "empty_slots": 24, "free_bikes": 11, "lat": 37.8045623549303, "total_slots": 35}
CityBikes/Grand Ave at Santa Clara Ave {"last_updated": "2017-12-03 09:22", "lon": -122.2472152, "percent_full": 52, "empty_slots": 8, "free_bikes": 9, "lat": 37.8127441, "total_slots": 17}
CityBikes/Telegraph Ave at 27th St {"last_updated": "2017-12-03 06:54", "lon": -122.26788640022278, "percent_full": 38, "empty_slots": 11, "free_bikes": 7, "lat": 37.816073115011406, "total_slots": 18}
CityBikes/Bay Pl at Vernon St {"last_updated": "2017-12-03 10:01", "lon": -122.26077854633331, "percent_full": 26, "empty_slots": 17, "free_bikes": 6, "lat": 37.81231409135146, "total_slots": 23}
CityBikes/19th Street BART Station {"last_updated": "2017-12-03 09:47", "lon": -122.2682473, "percent_full": 17, "empty_slots": 29, "free_bikes": 6, "lat": 37.8090126, "total_slots": 35}
CityBikes/Telegraph Ave at 19th St {"last_updated": "2017-12-02 23:18", "lon": -122.2699271, "percent_full": 56, "empty_slots": 11, "free_bikes": 14, "lat": 37.8087021, "total_slots": 25}
CityBikes/Grand Ave at Webster St {"last_updated": "2017-12-03 09:59", "lon": -122.2651925, "percent_full": 28, "empty_slots": 18, "free_bikes": 7, "lat": 37.8113768, "total_slots": 25}

```
# Dependencies
* paho-mqtt==1.3.1
* python-citybikes==0.1.3
* DateTime==4.2
* simplejson==3.13.2
