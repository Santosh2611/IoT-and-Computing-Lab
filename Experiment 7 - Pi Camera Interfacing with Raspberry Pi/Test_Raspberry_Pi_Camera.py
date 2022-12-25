import picamera # Provides a pure Python interface to the Raspberry Pi camera module
import time # Provides various time-related functions
picam = picamera.PiCamera()

picam.start_preview() # Displays the preview overlay
time.sleep(30) # Suspends execution for the given number of seconds
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
