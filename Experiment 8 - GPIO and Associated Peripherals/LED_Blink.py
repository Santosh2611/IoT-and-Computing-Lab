# LED Blinking using Raspberry Pi

import RPi.GPIO as GPIO # Module to control the GPIO on a Raspberry Pi
import time # Provides various time-related functions
GPIO.setwarnings(False) # Disable warnings

# ledpin = 36 # Selecting a pin to be used for connecting LED
ledpin = 16

# GPIO.setmode(GPIO.BOARD) # Physical pin number numbering scheme is followed
GPIO.setmode(GPIO.BCM) # For GPIO numbering, choose BCM

GPIO.setup(ledpin, GPIO.OUT) # Selected pin is configured as output

while True:
    GPIO.output(ledpin, True) # Turn the LED ON
    time.sleep(1) # Sleep for 1 Second
    GPIO.output(ledpin, False) # Turn the LED OFF
    time.sleep(1) # Sleep for 1 Second
    
GPIO.cleanup() # Clear GPIO pins