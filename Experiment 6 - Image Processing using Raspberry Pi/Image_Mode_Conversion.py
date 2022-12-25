from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit.
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file

res = im.convert("L") # Returns a converted copy of the image, translating a color image to greyscale
root = tk.Tk() # Construct a toplevel Tk widget
root.title("Colorspace Conversion Demo") # Refers to the name provided to the window
photo = ImageTk.PhotoImage(res) # A Tkinter-compatible photo image

l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images
l.pack() # Organizes widgets in blocks before placing them in the parent widget
l.photo=photo
root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
