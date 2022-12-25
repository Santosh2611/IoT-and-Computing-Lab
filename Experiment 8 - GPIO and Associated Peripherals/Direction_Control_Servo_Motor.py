# Direction Control of Servo Motor using PWM

import RPi.GPIO as GPIO # Module to control the GPIO on a Raspberry Pi
import time # Provides various time-related functions
GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BOARD) # Physical pin number numbering scheme is followed

motorpin = 12 # Pin to be connected to motor: GPIO 18
GPIO.setup(motorpin, GPIO.OUT) # Selected pin is configured as output
servo = GPIO.PWM(motorpin, 50) # Pin number, frequency in Hz
servo.start(0) # Start PWM signal generation with 0% duty cycle

try:
    while(True):
        for i in range(0, 100, 5): # Increase duty cycle from 0 to 100
            servo.ChangeDutyCycle(i) # Change duty cycle
            time.sleep(0.2) # Suspend execution for a given number of seconds
            
except KeyboardInterrupt: # Exception Handling
    print("Motor Stopped!")
    servo.stop() # Turn PWM OFF
    GPIO.cleanup() # Resets GPIO pins
    