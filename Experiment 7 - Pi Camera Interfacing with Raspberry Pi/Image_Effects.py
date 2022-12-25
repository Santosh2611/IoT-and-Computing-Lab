import picamera # Provides a pure Python interface to the Raspberry Pi camera module
from picamera import Color # The Color class is a tuple which represents a color as red, green, and blue components
import time # Provides various time-related functions
picam = picamera.PiCamera()
picam.start_preview(alpha = 200) # Retrieves or sets the opacity of the renderer

for effect in picam.EXPOSURE_MODES: # exposure_mode, awb_mode, image_effect, ....
    picam.exposure_mode = effect # Retrieves or sets the exposure mode of the camera
    picam.annotate_text = "Effect: %s"%effect # Retrieves or sets a text annotation for all output
    time.sleep(2) # Suspends execution for the given number of seconds
    
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
