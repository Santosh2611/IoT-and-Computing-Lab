from PIL import Image # Provides a class with the same name which is used to represent a PIL image
im = Image.open('Sample_Image_Web.tiff') # Opens and identifies the given image file
face_box = (100,100,300,300)
face = im.crop(face_box) # Returns a rectangular region from the image. 

rotated_face = face.transpose(Image.Transpose.ROTATE_180) # Transpose image (flip or rotate in 90-degree steps)
# PARAMETERS: method – One of Transpose.FLIP_LEFT_RIGHT, Transpose.FLIP_TOP_BOTTOM, Transpose.ROTATE_90,
# Transpose.ROTATE_180, Transpose.ROTATE_270, Transpose.TRANSPOSE or Transpose.TRANSVERSE

im.paste(rotated_face,face_box) # Pastes another image into the image.
im.show() # Displays the image
