from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
from PIL import ImageFilter # Contains definitions for a pre-defined set of filters, which can be be used with the Image.filter() method
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit.

def show_value(blur_radius):
    print('Gaussian Blur Radius: ', blur_radius)
    custom_filter = ImageFilter.GaussianBlur(radius=float(blur_radius)) # Blurs the image with a sequence of extended box filters
    img = im.filter(custom_filter) # Filters this image using the given filter
    photo = ImageTk.PhotoImage(img) # A Tkinter-compatible photo image
    l['image']=photo
    l.photo=photo

root = tk.Tk() # Construct a toplevel Tk widget
root.title('Gaussian Blur Filter Demo') # Refers to the name provided to the window
im = Image.open('/home/pi/Documents/CB.EN.U4CCE20053/Sample_Image_Web.tiff') # Opens and identifies the given image file
photo = ImageTk.PhotoImage(im) # A Tkinter-compatible photo image

l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images
l.pack() # Organizes widgets in blocks before placing them in the parent widget
l.photo=photo

# Provides a graphical slider object that allows you to select values from a specific scale:-
w = (tk.Scale(root, label="Gaussian Blur Radius", from_=0, to=5,
              resolution=1, command = show_value,
              orient=tk.HORIZONTAL))
w.pack() # Packs widgets relative to the earlier widget
root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
