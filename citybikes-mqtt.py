
#
# https://pypi.python.org/pypi/python-citybikes/0.1.3
# https://api.citybik.es/v2/
#
#
# CityBike -> MQTT
# Payload as JSON
#

import citybikes
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import simplejson as json
from datetime import datetime

mqtt_host = "localhost"
MQTT_AUTH = {
    'username':'XXX',
    'password':'XXX'
}


# Check City Bikes API docs
networkuid = 'ford-gobike'

client = citybikes.Client()
network = citybikes.Network(client, uid=networkuid)
network = network['stations']

myStations = ["8302e5d11a6c84bac27a774de41474f9", \
               "c2648d0ffed4d1f710ccaf79e9a304fa", \
               "3f5c0437929a0f6dbc32f116850a4196", \
               "36aa8ab83177d5f5beb83685c7f645d3"]


for station in network:
        for id in myStations:
                if id == station['id']:
                        topic = "CityBikes/" + station['name']
                        payload = json.dumps({  'free_bikes':station['free_bikes'], \
                                                'empty_slots':station['empty_slots'], \
                                                'lat':station['latitude'], \
                                                'lon':station['longitude'], \
                                                'last_updated':datetime.fromtimestamp(station['extra']['last_updated']).strftime('%Y-%m-%d %H:%M')})
                        
                        #print(station['name'])
                        #print(payload)
                        publish.single(topic,payload=payload,hostname=mqtt_host,client_id="citybikesbot",auth=MQTT_AUTH,port=1883,protocol=mqtt.MQTTv311)

