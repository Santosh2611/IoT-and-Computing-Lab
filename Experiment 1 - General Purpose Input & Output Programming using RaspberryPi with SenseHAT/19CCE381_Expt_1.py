# Import Necessary Libraries:-
from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF

from time import sleep # Handle time-related tasks

# Hello World Display on SenseHAT:-
yellow = (255,255,0) 
blue = (0,0,255)

sense.show_message("Hello", scroll_speed = 0.1, # Control Scroll Speed; Greater speed implies slower scroll time
                   text_colour = yellow, # Text Colour
                   back_colour = blue) # Background Colour
sleep(3) # Wait for three seconds

sense.show_message("World", scroll_speed = 0.1, # Control Scroll Speed; Greater speed implies slower scroll time
                   text_colour = yellow, # Text Colour
                  back_colour = blue) # Background Colour
sleep(3) # Wait for three seconds

sense.clear() # Clear everything

# Single Character Displayed followed by Rotation and Flip:-
sense.show_letter("Z", # Displays a single text character on the LED matrix
                  text_colour = yellow, # Text Colour
                  back_colour = blue) # Background Colour)

sense.flip_h() # Horizontal Flip
sense.flip_v() # Vertical Flip
sense.set_rotation(180) # Rotate character by 180 degrees

# Single Pixel activation in SenseHAT:-
sense.set_pixel(1,2,blue) # First Column, Second Row, Blue Colour

# Custom Character Creation using LED Matrix (Print the letter 'S'):-
sense.set_pixel(0,0,blue); sense.set_pixel(1,0,blue); sense.set_pixel(2,0,blue); sense.set_pixel(3,0,blue); sense.set_pixel(4,0,blue); sense.set_pixel(5,0,blue); sense.set_pixel(6,0,blue); sense.set_pixel(7,0,blue)
sense.set_pixel(0,1,blue); sense.set_pixel(0,2,blue)
sense.set_pixel(0,3,blue); sense.set_pixel(1,3,blue); sense.set_pixel(2,3,blue); sense.set_pixel(3,3,blue); sense.set_pixel(4,3,blue); sense.set_pixel(5,3,blue); sense.set_pixel(6,3,blue); sense.set_pixel(7,3,blue)
sense.set_pixel(0,4,blue); sense.set_pixel(1,4,blue); sense.set_pixel(2,4,blue); sense.set_pixel(3,4,blue); sense.set_pixel(4,4,blue); sense.set_pixel(5,4,blue); sense.set_pixel(6,4,blue); sense.set_pixel(7,4,blue)
sense.set_pixel(7,5,blue); sense.set_pixel(7,6,blue)
sense.set_pixel(0,7,blue); sense.set_pixel(1,7,blue); sense.set_pixel(2,7,blue); sense.set_pixel(3,7,blue); sense.set_pixel(4,7,blue); sense.set_pixel(5,7,blue); sense.set_pixel(6,7,blue); sense.set_pixel(7,7,blue)

# Position and Action Display of Joystick:-
while True:
    for event in sense.stick.get_events(): # Returns a list of InputEvent tuples representing all events that have occurred since the last call to get_events or wait_for_event
        # direction - The direction the joystick was moved, as a string ("up", "down", "left", "right", "middle")
        # action - The action that occurred, as a string ("pressed", "released", "held")
        print(event.direction, event.action)
        
# Character Display based on Position and Action of Joystick:-
while True:
    for event in sense.stick.get_events():
        if (event.direction == "middle" and event.action == "held"):           
           sense.show_letter("Z",
                             text_colour = yellow, # Text Colour
                             back_colour = blue) # Background Colour
           
# SenseHAT Led Matrix Control based on Position and Action of Joystick using Function:-
def red(): # Sets the entire LED matrix to red colour
    sense.clear(255,0,0)
    
def green(): # Sets the entire LED matrix to green colour
    sense.clear(0,255,0)
    
def blue(): # Sets the entire LED matrix to blue colour
    sense.clear(0,0,255)
    
def yellow(): # Sets the entire LED matrix to yellow colour
    sense.clear(255,255,0)
    
# Tell the program which function to associate with which direction:-
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear # Press the enter key

# Digital Input Operations Using Joystick:-
while True:
    for event in sense.stick.get_events():
       print(event.direction, event.action)
       
       if (event.direction == "middle" and event.action == "held"):
           yellow = (255,255,0); blue = (0,0,255) # Initialize the colours
           sense.show_letter("Z",
                             text_colour = yellow, # Text Colour
                            back_colour = blue) # Background Colour
       else:
            sense.clear() # Clear everything

while True:
    pass # This keeps the program running to receive the joystick events.

# Assignment: To implement a counter which displays the count on the led matrix.
#             The count needs to be incremented on pressing the joystick's right key,
#             it should get decremented on pressing the joystick's left key and
#             should get cleared to zero when the joystick's middle key is pressed.

count = 0 # Initialize the counter variable to zero
yellow = (255,255,0); blue = (0,0,255) # Initialize the colours

def increment_value():
    global count
    count = count + 1
    sense.show_letter(str(count),
                   text_colour = yellow, # Text Colour
                   back_colour = blue) # Background Colour
    
def decrement_value():
    global count
    count = count - 1
    sense.show_letter(str(count),
                   text_colour = yellow, # Text Colour
                   back_colour = blue) # Background Colour
    
# Tell the program which function to associate with which direction:-
sense.stick.direction_up = increment_value
sense.stick.direction_down = decrement_value
sense.stick.direction_middle = sense.clear # Press the enter key

while True:
    pass # This keeps the program running the receive joystick events
