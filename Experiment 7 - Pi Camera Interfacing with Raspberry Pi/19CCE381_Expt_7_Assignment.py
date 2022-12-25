import picamera # Provides a pure Python interface to the Raspberry Pi camera module
from picamera import Color # The Color class is a tuple which represents a color as red, green, and blue components
import time # Provides various time-related functions

from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
from PIL import ImageFilter # Contains definitions for a pre-defined set of filters, which can be be used with the Image.filter() method
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit

def blur_image(blur_radius):
    print('Gaussian Blur Radius: ', blur_radius)
    custom_filter = ImageFilter.GaussianBlur(radius=float(blur_radius)) # Blurs the image with a sequence of extended box filters
    img = im.filter(custom_filter) # Filters the image using the given filter
    photo = ImageTk.PhotoImage(img) # A Tkinter-compatible photo image
    l['image']=photo
    l.photo=photo

def rotate_image(angle):
    print('Angle: ',angle)
    img = im.rotate(float(angle)) # Returns a rotated copy of the image
    photo = ImageTk.PhotoImage(img) # A Tkinter-compatible photo image
    l['image']=photo
    l.photo=photo

def emboss_image(emboss_value):
    print('Emboss Value: ', emboss_value)
    custom_filter = ImageFilter.EMBOSS() # Apply emboss filter on to the image
    img = im.filter(custom_filter) # Filters the image using the given filter
    photo = ImageTk.PhotoImage(img) # A Tkinter-compatible photo image
    l['image']=photo
    l.photo=photo
    
picam = picamera.PiCamera()
picam.rotation = 180 # Retrieves or sets the current rotation of the camera’s image
picam.start_preview(alpha = 200) # Retrieves or sets the opacity of the renderer
time.sleep(5) # Suspends execution for the given number of seconds

picam.capture("Rotated_Image.png", resize=(800,450)) # Capture an image from the camera, storing it in output
picam.stop_preview() # Hides the preview overlay
picam.close() # Finalizes the state of the camera
    
root = tk.Tk() # Construct a toplevel Tk widget
root.title('Assignment Demo') # Refers to the name provided to the window
im = Image.open('Rotated_Image_Assignment.tiff') # Opens and identifies the given image file
photo = ImageTk.PhotoImage(im) # A Tkinter-compatible photo image

l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images

# Organizes widgets in a table-like structure in the parent widget:-
l.grid(column=50, # The column to put widget in; default 0 (leftmost column)
       row=0, # The row to put widget in; default the first row that is still empty
       padx=5, # How many pixels to pad widget, horizontally and vertically, outside v's borders
       sticky='n') # What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell.
                   # sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.

l.photo=photo

# Provides a graphical slider object that allows you to select values from a specific scale:-
# Organizes widgets in a table-like structure in the parent widget:-

image_blur = (tk.Scale(root, label="Gaussian Blur Radius", from_=0, to=5, resolution=1, command=blur_image, orient=tk.VERTICAL))
image_blur.grid(column=0, row=0, padx=5, sticky='w')

rotate_image = (tk.Scale(root, label="Angle", from_=0, to=360, resolution=1, command = rotate_image, orient=tk.HORIZONTAL))
rotate_image.grid(column=50, row=10, padx=5, sticky='s')

image_emboss = (tk.Scale(root, label="Emboss Value", from_=0, to=1, resolution=1, command = emboss_image, orient=tk.VERTICAL))
image_emboss.grid(column=60, row=0, padx=5, sticky='e')

root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
