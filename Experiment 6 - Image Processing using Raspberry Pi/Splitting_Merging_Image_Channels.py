from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file

root = tk.Tk() # Construct a toplevel Tk widget
root.title("RED Channel Demo") # Refers to the name provided to the window
r,g,b = im.split() # Split the image into individual bands

photo_1 = ImageTk.PhotoImage(im) # A Tkinter-compatible photo image
l_1 = tk.Label(root, image=photo_1) # Widget that is used to implement display boxes where you can place text or images
l_1.pack() # Organizes widgets in blocks before placing them in the parent widget
l_1.photo=photo_1

photo_2 = ImageTk.PhotoImage(Image.merge("RGB",(r,g,b))) # Merge a set of single band images into a new multiband image
l_2 = tk.Label(root, image=photo_2) # Widget that is used to implement display boxes where you can place text or images
l_2.pack() # Organizes widgets in blocks before placing them in the parent widget
l_2.photo=photo_2

root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
