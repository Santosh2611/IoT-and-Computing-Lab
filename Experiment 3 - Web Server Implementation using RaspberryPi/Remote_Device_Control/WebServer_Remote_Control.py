from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

from flask import Flask # A lightweight Web Server Gateway Interface (WSGI) web application framework
from flask import render_template # Used to generate output from a template file that is found in the application's templates folder. 
app = Flask(__name__) # Flask constructor takes the name of current module (__name__) as argument.

@app.route('/') # Map the URLs to a specific function that will handle the logic for that URL.
def index():
    deviceSts = "OFF"
    sense.show_letter("I")
    templateData = {'device1' : deviceSts}
    return render_template('index.html',**templateData)
#   return render_template('index.html',**weatherData)

@app.route("/<deviceName>/<action>") # Map the URLs to a specific function that will handle the logic for that URL.
def action(deviceName, action):
    if deviceName == 'd1' and action == 'on':
        deviceSts = "ON"
        sense.show_letter("O") # Up Arrow
    if deviceName == 'd1' and action == 'off':
        deviceSts = "OFF"
        sense.show_letter("F") # Up Arrow
    templateData = {'device1' : deviceSts}
    return render_template('index.html',**templateData)

@app.route('/off') # Map the URLs to a specific function that will handle the logic for that URL.
def clear():
    deviceSts = "OFF"
    sense.clear() # No arguments defaults to OFF
    templateData = {'device1' : deviceSts}
    return render_template('index.html',**templateData)

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
