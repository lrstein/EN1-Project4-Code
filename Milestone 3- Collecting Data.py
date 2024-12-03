import network
from umqttsimple import MQTTClient
from time import sleep
import time

wlan = network.WLAN(network.STA_IF)

if not wlan.isconnected():
    wlan.active(True)

    ssid = "Tufts_Wireless"
    print("Connecting to {}...".format(ssid))
    wlan.connect(ssid)
    while not wlan.isconnected():
        sleep(1)
        print('.')

print("Connected!")
print("IP address:", wlan.ifconfig()[0])

mqtt_server = "bell-iot.eecs.tufts.edu"

clientId = "esp32-lstein"

client = MQTTClient(clientId, mqtt_server)
client.connect()

client.publish(clientId + '/ip', wlan.ifconfig()[0])

from machine import Pin
from thermocouple import MAX31855

#pins on breadboard for both thermocouples
fridge = MAX31855(cs=Pin(21), sck=Pin(38), so=Pin(35))
freezer = MAX31855(cs=Pin(3), sck=Pin(1), so=Pin(5))

hours = 3
#gets current time
start = time.time()
#calculates when end is based on current time and runtime preference
end = start + (60*60*hours)

#while loop becomes alarm clock, running until current time has reached desired end time
while (time.time() < end):
    #converts celsius to fahrenheit because .read() defaults to celsius
    farFridge = (fridge.read() * (9/5)) + 32
    farFreezer = (freezer.read() * (9/5)) + 32
    #collect and publish data to website under respective topic names
    client.publish(clientId + '/fridge_dial1to2_2', str(farFridge))
    client.publish(clientId + '/freezer_dial1to2_2', str(farFreezer))
    #sleep for 15 seconds before collecting next row of data
    time.sleep(15)

#prints "Done!" to alert user that data collection has finished running
print("Done!")