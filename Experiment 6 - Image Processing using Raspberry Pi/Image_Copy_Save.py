from PIL import Image # Provides a class with the same name which is used to represent a PIL image
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file
im_temp = im.copy() # Copies the image
im_temp.save("Image_Save.tiff") # Saves the image under the given filename
