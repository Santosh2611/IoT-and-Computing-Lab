from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

import sys # Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME = 'XXXXXXXXXX' # Username
ADAFRUIT_IO_KEY = 'XXXXXXXXXX' # Active Key
FEED_ID = 'XXXXXXXXXX-lab' # Key from Feeds

# Define callback functions which will be called when certain events happen:-
def connected(client): # Will be called when the client connects
    print('Connected to Adafruit IO! Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID) # Subscribe to a feed
    
def disconnected(client): # Will be called when the client disconnects
    print('Disconnected from Adafruit IO!')
    sys.exit(1) # Optional argument arg can be an integer giving the exit or another type of object; Zero is considered “successful termination”
    
def message(client, feed_id, payload): # Will be called when a subscribed feed has a new value
    
    # The feed_id parameter identifies the feed, and the payload parameter has the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    
    if payload == "1":
        print("Light ON")
        sense.show_letter("O") # Display a single text character on the LED matrix
        
    if payload == "0":
        print("Light OFF")
        sense.clear() # No arguments defaults to OFF
        
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect() # Opens a new MQTT connection to the specified broker
client.loop_blocking()
