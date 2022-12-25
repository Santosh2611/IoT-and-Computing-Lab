import picamera # Provides a pure Python interface to the Raspberry Pi camera module
from picamera import Color # The Color class is a tuple which represents a color as red, green, and blue components
import time # Provides various time-related functions
picam = picamera.PiCamera()
picam.start_preview() # Displays the preview overlay

for i in range(-100,100):
    picam.annotate_text="Contrast: %s"%i # Retrieves or sets a text annotation for all output
    picam.contrast=i # Retrieves or sets the contrast setting of the camera
    time.sleep(0.1) # Suspends execution for the given number of seconds
    
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
