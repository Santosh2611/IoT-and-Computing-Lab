import picamera # Provides a pure Python interface to the Raspberry Pi camera module
import time # Provides various time-related functions
picam = picamera.PiCamera()

picam.rotation = 180 # Retrieves or sets the current rotation of the camera’s image
picam.start_preview(alpha = 200) # Retrieves or sets the opacity of the renderer
time.sleep(5) # Suspends execution for the given number of seconds

picam.capture("Rotated_Image.png") # Capture an image from the camera, storing it in output
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
