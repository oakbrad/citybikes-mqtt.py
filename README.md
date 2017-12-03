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
CityBikes/Frank H Ogawa Plaza {"lat": 37.8045623549303, "last_updated": "2017-12-02 17:38", "lon": -122.27173805236816, "empty_slots": 7, "free_bikes": 28}
CityBikes/Franklin St at 9th St {"lat": 37.8005161, "last_updated": "2017-12-02 15:43", "lon": -122.2720799, "empty_slots": 26, "free_bikes": 1}
CityBikes/Lake Merritt BART Station {"lat": 37.7973195, "last_updated": "2017-12-02 17:26", "lon": -122.2653199, "empty_slots": 14, "free_bikes": 13}
CityBikes/Washington St at 8th St {"lat": 37.8007544, "last_updated": "2017-12-02 15:37", "lon": -122.2748943, "empty_slots": 13, "free_bikes": 14}
CityBikes/Frank H Ogawa Plaza {"lat": 37.8045623549303, "last_updated": "2017-12-02 17:46", "lon": -122.27173805236816, "empty_slots": 6, "free_bikes": 29}
CityBikes/Franklin St at 9th St {"lat": 37.8005161, "last_updated": "2017-12-02 15:43", "lon": -122.2720799, "empty_slots": 26, "free_bikes": 1}
CityBikes/Lake Merritt BART Station {"lat": 37.7973195, "last_updated": "2017-12-02 17:26", "lon": -122.2653199, "empty_slots": 14, "free_bikes": 13}
CityBikes/Washington St at 8th St {"lat": 37.8007544, "last_updated": "2017-12-02 15:37", "lon": -122.2748943, "empty_slots": 13, "free_bikes": 14}
```
# Dependencies
* paho-mqtt==1.3.1
* python-citybikes==0.1.3
* DateTime==4.2
* simplejson==3.13.2
