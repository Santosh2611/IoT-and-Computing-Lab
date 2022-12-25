import sys
import time
import random
from time import sleep
from Adafruit_IO import MQTTClient, Client, Feed
from sense_hat import SenseHat
sense = SenseHat()

ADAFRUIT_IO_KEY = 'aio_UbWq26heRtiVBiS3FsHsabCmlFrW'
ADAFRUIT_IO_USERNAME = 'Santosh_53'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
FEED_ID = 'home-automation-system' # Adafruit 'Feed-Key'
READ_TIMEOUT = 5

pressure_feed = aio.feeds('pressure') # 'Pressure' is IO Feed created in Adafruit
humidity_feed = aio.feeds('humidity') # 'Humidity' is IO Feed created in Adafruit

def connected(client):
        print('Connected to Adafruit IO! Listening for {0} changes...'.format(FEED_ID))
        client.subscribe(FEED_ID)
        
def disconnected(clinet):
    print('Disconnected fro Adafruit IO!')
    sys.exit(1)
    
def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

    while True:
        
        val = random.randint(1,30)
        pressure = val
        humidity = val
        
        if payload == "1":
            print("Light ON")
            sense.show_letter("O")
        
        if payload == "0":
            print("Light OFF")
            sense.clear()
        
        if humidity is not None and pressure is not None:
            print('Pressure = (0:0.1f) Pascal \n Humidity = (1:0.1f)%'.format(pressure, humidity))
            
            # Send pressure and humidity feeds to Adafruit IO:-
            pressure = '%.2f'%(pressure)
            humidity = '%.2f'%(humidity)
            aio.send(pressure_feed.key, str(pressure))
            aio.send(humidity_feed.key, str(humidity))
            
        else:
            print('Failed to get Pressure and Humidity Data form SenseHat')
        time.sleep(READ_TIMEOUT) # Timeout to avoid flooding Adafruit IO
                
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_message = message
client.connect()
client.on_disconnect = disconnected
client.loop_blocking()
