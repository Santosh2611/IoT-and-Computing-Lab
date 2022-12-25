from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file

print(im.mode) # String specifying the pixel format used by the image
print(im.format) # File format of the source file
print(im.size) # Size in pixels is given as a 2-tuple (width, height)
print(im.info) # A dictionary holding data associated with the image
print(im.getbands()) # Returns a tuple containing the name of each band in the image

root = tk.Tk() # Construct a toplevel Tk widget
root.title("Display Image") # Refers to the name provided to the window
photo = ImageTk.PhotoImage(im) # A Tkinter-compatible photo image

l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images
l.pack() # Organizes widgets in blocks before placing them in the parent widget
l.photo=photo
root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
