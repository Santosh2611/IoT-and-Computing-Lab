import json # Can be used to work with JSON (JavaScript Object Notation) data
import requests # Allows you to send HTTP/1.1 requests extremely easily
import threading # Constructs higher-level threading interfaces on top of the lower level _thread module
import urllib.request # Defines functions and classes which help in opening URLs (mostly HTTP) in a complex world

from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

def thingspeak_post():
    
    threading.Timer(15,thingspeak_post).start() # Create a timer with interval and function as parameters
    pressure = sense.get_pressure() # Gets the current pressure in Millibars from the pressure sensor.
    humidity = sense.get_humidity() # Gets the percentage of relative humidity from the humidity sensor.
    
    URL='https://api.thingspeak.com/update?api_key=XXXXXXXXXX&field1=0' # Write a Channel Feed
    KEY='XXXXXXXXXX' # Write API Key    
    HEADER='&field1={}&field2={}'.format(pressure,humidity)
    
    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)    
    data = urllib.request.urlopen(NEW_URL)
    print(data)
    
# Driver Code - Main Function:-
if __name__ == '__main__':
    thingspeak_post()
