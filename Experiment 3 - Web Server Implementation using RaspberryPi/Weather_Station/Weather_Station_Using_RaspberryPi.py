from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

from flask import Flask # A lightweight Web Server Gateway Interface (WSGI) web application framework
from flask import render_template # Used to generate output from a template file that is found in the application's templates folder. 
app = Flask(__name__) # Flask constructor takes the name of current module (__name__) as argument.

import time # This module provides various time-related functions.

# Initialize the colours:-
green = (0,255,0)
nothing = (0,0,0)

@app.route('/') # Map the URLs to a specific function that will handle the logic for that URL.
def index():
    
    pressure = sense.get_pressure() # Gets the current pressure in Millibars from the pressure sensor.
    temperature = sense.get_temperature() # Gets the temperature in Degrees from the temperature sensor.
    seconds = time.time() # Return the time in seconds since the epoch as a floating point number. 
    local_time = time.ctime(seconds) # Convert a time expressed in seconds since the epoch to a string of a form:
                                     #'Sun Jun 20 23:21:05 1993' representing local time.
    
    print_message = str("Weather Monitoring System!" + "\n" +
                    "Current Pressure: " + str(round(pressure, 2)) + " millibars" + "\n" +
                    "Temperature: " + str(round(temperature, 2)) + " degree(s)" + "\n" +
                    "Local Time: " + str(local_time))

    sense.show_message("Current Pressure: {} Temperature: {} Local Time: {}".format(pressure, temperature, local_time),
                       scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                       text_colour = green, # Text Colour
                       back_colour = nothing) # Background Colour
    
    weatherData = {'weather': print_message}    
    return render_template('index.html',**weatherData)

# pi@raspberrypi:~ $ ifconfig
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 172.17.126.47  netmask 255.255.255.0  broadcast 172.17.126.255
#         inet6 fe80::9d5a:ccdd:c209:ebab  prefixlen 64  scopeid 0x20<link>
#         ether e4:5f:01:c6:82:70  txqueuelen 1000  (Ethernet)
#         RX packets 6705  bytes 8236015 (7.8 MiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 2716  bytes 278737 (272.2 KiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# Driver Code - Main Function:-
if __name__ == '__main__':
    app.run(host='172.17.126.47') # Port Number - 5000
