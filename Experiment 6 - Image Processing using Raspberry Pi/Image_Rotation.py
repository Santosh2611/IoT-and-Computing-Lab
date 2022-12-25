from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageTk # Contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
import tkinter as tk # Standard Python interface to the Tcl/Tk GUI toolkit.

def show_value(angle):
    print('Angle: ', angle)
    img = im.rotate(float(angle)) # Returns a rotated copy of the image
    photo = ImageTk.PhotoImage(img) # A Tkinter-compatible photo image
    l['image']=photo
    l.photo=photo

root = tk.Tk() # Construct a toplevel Tk widget
root.title('Rotation Demo') # Refers to the name provided to the window
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file
photo = ImageTk.PhotoImage(im) # A Tkinter-compatible photo image

l = tk.Label(root, image=photo) # Widget that is used to implement display boxes where you can place text or images
l.pack() # Organizes widgets in blocks before placing them in the parent widget
l.photo=photo

# Provides a graphical slider object that allows you to select values from a specific scale:-
w = (tk.Scale(root,
              label="Angle", # You can display a label within the scale widget by setting this option to the label's text
              from_=0, # A float or integer value that defines one end of the scale's range
              to=360, # A float or integer value that defines one end of the scale's range; Can be either greater than or less than the from_ value
              resolution=1,
              command = show_value, # A procedure to be called every time the slider is moved
              orient=tk.HORIZONTAL) # Scale runs along the x dimension
     )

w.pack() # Packs widgets relative to the earlier widget
root.mainloop() # Loop forever, waiting for events from the user, until the user exits the program
