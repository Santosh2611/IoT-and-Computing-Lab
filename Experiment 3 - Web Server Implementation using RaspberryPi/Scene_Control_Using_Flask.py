from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF
sense.low_light = True # Toggles the LED matrix in low light mode, useful if the Sense HAT is being used in a dark environment.

from flask import Flask # Lightweight Web Server Gateway Interface (WSGI) web application framework
app = Flask(__name__) # Flask constructor takes the name of current module (__name__) as argument.

# Initialize the colours:-
green = (0,255,0)
red = (255,0,0)
nothing = (0,0,0)

def scene_keep_out():
    R = red
    scene = [
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R]
    return scene
    
def scene_come_in():
    G = green
    scene = [
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G]
    return scene

def scene_off():
    N = nothing
    scene = [
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N,
        N,N,N,N,N,N,N,N]
    return scene

@app.route('/') # Map the URLs to a specific function that will handle the logic for that URL.
def hello_world():
    return 'Lighting Scene Controller!'

@app.route('/keep-out') # Map the URLs to a specific function that will handle the logic for that URL.
def keep_out():
    sense.set_pixels(scene_keep_out())
    return 'Keep Out Set'

@app.route('/come-in') # Map the URLs to a specific function that will handle the logic for that URL.
def come_in():
    sense.set_pixels(scene_come_in())
    return 'Ok To Come In Set'

@app.route('/off') # Map the URLs to a specific function that will handle the logic for that URL.
def off():
    sense.set_pixels(scene_off())
    return 'Off'

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
    