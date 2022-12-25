from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit.

root = tk.Tk() # Construct a toplevel Tk widget
root.title('Transpose Demo') # Refers to the name provided to the window
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file

out = im.transpose(Image.Transpose.ROTATE_180) # Transpose image (flip or rotate in 90-degree steps)
# PARAMETERS: method – One of Transpose.FLIP_LEFT_RIGHT, Transpose.FLIP_TOP_BOTTOM, Transpose.ROTATE_90,
# Transpose.ROTATE_180, Transpose.ROTATE_270, Transpose.TRANSPOSE or Transpose.TRANSVERSE

photo = ImageTk.PhotoImage(out) # A Tkinter-compatible photo image
l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images
l.pack() # Organizes widgets in blocks before placing them in the parent widget
l.photo=photo
