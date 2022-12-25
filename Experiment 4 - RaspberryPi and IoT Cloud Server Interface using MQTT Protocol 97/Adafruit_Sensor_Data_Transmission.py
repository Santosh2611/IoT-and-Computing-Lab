from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

# Import library and create instance of REST client:-
from Adafruit_IO import Client, Feed
ADAFRUIT_IO_USERNAME = 'XXXXXXXXXX' # Username
ADAFRUIT_IO_KEY = 'XXXXXXXXXX' # Active Key
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

import time # Provides various time-related functions
import random # Implements pseudo-random number generators for various distributions
READ_TIMEOUT = 5

# Get list of feeds:-
pressure_feed = aio.feeds('pressure') # 'pressure' is IO Feed created in Adafruit
humidity_feed = aio.feeds('humidity') # 'humidity' is IO Feed created in Adafruit

while True:
    
    val = random.randint(1,30) # Returns an integer number selected element from the specified range; Alias for randrange(start, stop+1)
    pressure = val
    humidity = val
    
    if humidity is not None and pressure is not None:
        print('Pressure = (0:0.1f) Pascal \n Humidity = (1:0.1f)%'.format(pressure, humidity))
        
        # Send pressure and humidity feeds to Adafruit IO:-
        pressure = '%.2f'%(pressure)
        humidity = '%.2f'%(humidity)
        aio.send(pressure_feed.key, str(pressure))
        aio.send(humidity_feed.key, str(humidity))
        
    else:
        print('Failed to get Pressure and Humidity Data from SenseHat!')
        
    time.sleep(READ_TIMEOUT) # Timeout to avoid flooding Adafruit IO
    
