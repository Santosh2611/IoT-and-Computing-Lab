# LED Control using Switch

import RPi.GPIO as GPIO # Module to control the GPIO on a Raspberry Pi
import time # Provides various time-related functions
GPIO.setwarnings(False) # Disable warnings

ledpin = 36
switch = 40

GPIO.setmode(GPIO.BOARD) # Physical pin number numbering scheme is followed
GPIO.setup(ledpin, GPIO.OUT) # Selected pin is configured as output
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Enable pull

while True:
    status = GPIO.input(switch) # Read status of pin/port and assign to variable switch  
    if(status):
        GPIO.output(ledpin, True) # Turn the LED ON
        print("LED ON: Button Pressed!")
    else:
        GPIO.output(ledpin, False) # Turn the LED OFF
        print("Button NOT Pressed!")
        
GPIO.cleanup() # Clear GPIO pins