from PIL import Image # Provides a class with the same name which is used to represent a PIL image
from PIL import ImageFilter
im = Image.open('/home/pi/Documents/CB.EN.U4CCE20053/Sample_Image_Web.tiff') # Opens and identifies the given image file
im_temp = im.filter(ImageFilter.BLUR) # Filters this image using the given filter
im_temp.show() # Saves this image under the given filename
