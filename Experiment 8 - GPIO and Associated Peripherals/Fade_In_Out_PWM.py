# LED Fade In and Fade Out using PWM

import RPi.GPIO as GPIO # Module to control the GPIO on a Raspberry Pi
import time # Provides various time-related functions
GPIO.setwarnings(False) # Disable warnings

ledpin = 32
GPIO.setmode(GPIO.BOARD) # Physical pin number numbering scheme is followed
GPIO.setup(ledpin, GPIO.OUT) # Selected pin is configured as output

dimmer = GPIO.PWM(ledpin, 50) # Pin number, frequency in Hz
dimmer.start(0) # Start PWM signal generation with 0% duty cycle
try:
    while(True):
        
        for i in range(0, 100, 5): # Increase duty cycle from 0 to 100
            dimmer.ChangeDutyCycle(i) # Change duty cycle
            time.sleep(0.2) # Suspend execution for a given number of seconds
        
        for i in range(100, 0, -5): # Decrease duty cycle from 100 to 0
            dimmer.ChangeDutyCycle(i) # Change duty cycle
            time.sleep(0.2) # Suspend execution for a given number of seconds
            
except KeyboardInterrupt: # Exception Handling
    dimmer.stop() # Turn PWM OFF
    GPIO.cleanup() # Resets GPIO pins
    