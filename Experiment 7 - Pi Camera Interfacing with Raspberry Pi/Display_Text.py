import picamera # Provides a pure Python interface to the Raspberry Pi camera module
from picamera import Color # The Color class is a tuple which represents a color as red, green, and blue components
import time # Provides various time-related functions
picam = picamera.PiCamera()
picam.start_preview() # Displays the preview overlay

picam.annotate_text = "Hello From Raspberry Pi!" # Retrieves or sets a text annotation for all output
picam.annotate_text_size=60 # Controls the size of the annotation text
picam.annotate_background=Color('blue') # Controls what background is drawn behind the annotation
picam.annotate_foreground=Color('yellow') # Controls the color of the annotation text

time.sleep(5) # Suspends execution for the given number of seconds
picam.capture('Text_Image.png') # Capture an image from the camera, storing it in output
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
