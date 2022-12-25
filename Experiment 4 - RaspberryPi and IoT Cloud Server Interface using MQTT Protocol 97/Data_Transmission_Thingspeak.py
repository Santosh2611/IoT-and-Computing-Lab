import json # Can be used to work with JSON (JavaScript Object Notation) data
import random # Implements pseudo-random number generators for various distributions
import requests # Allows you to send HTTP/1.1 requests extremely easily
import threading # Constructs higher-level threading interfaces on top of the lower level _thread module
import urllib.request # Defines functions and classes which help in opening URLs (mostly HTTP) in a complex world

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start() # Create a timer with interval and function as parameters
    val=random.randint(1,30) # Returns an integer number selected element from the specified range; Alias for randrange(start, stop+1)
    URL='https://api.thingspeak.com/update?api_key=XXXXXXXXXX&field1=0' # Write a Channel Feed
    KEY='XXXXXXXXXX' # Write API Key
    
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)
    
    data = urllib.request.urlopen(NEW_URL) # Open the URL, which can be either a string or a Request object
    print(data)

# Driver Code - Main Function:-
if __name__ == '__main__':
    thingspeak_post()
    