# Display Scrolling Text on LCD

# sudo pip install adafruit-circuitpython-charlcd
import time # Provides various time-related functions
import board # Implements a general-purpose board structure which has the functionality needed for a range of purposes
import digitalio # Contains classes to provide access to basic digital IO

import adafruit_character_lcd.character_lcd as characterlcd # Module for interfacing with monochromatic character LCDs

# Modify this if you have a different sized character LCD:-
lcd_columns = 16; lcd_rows = 2

# Metro M0/M4 Pin Config:-
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_backlight = digitalio.DigitalInOut(board.D13)

# Initialise the LCD Class:-
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.backlight = True # Turn backlight on
lcd.message = "Hello\nCircuitPython" # Print a two line message
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD

lcd.text_direction = lcd.RIGHT_TO_LEFT # Print two line message right to left
lcd.message = "Hello\nCircuitPython"
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD

lcd.text_direction = lcd.LEFT_TO_RIGHT # Print two line message left to right
lcd.message = "Hello\nCircuitPython"
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD

lcd.cursor = True # True if cursor is visible
lcd.message = "Cursor!"
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD

lcd.blink = True # True to blink the cursor
lcd.message = "Blinky Cursor!"
time.sleep(5) # Wait for five seconds
lcd.blink = False # False to stop blinking
lcd.clear() # Clear my LCD

# Create message to scroll:-
scroll_msg = "<--Scroll"
lcd.message = scroll_msg

# Scroll message to the left:- 
for i in range(len(scroll_msg)):
    time.sleep(0.5) # Wait for half a second
    lcd.move_left() # Moves displayed text left one column
lcd.clear() # Clear my LCD

lcd.message = "Going to sleep\n C ya later !"
time.sleep(3) # Wait for three seconds
lcd.backlight = False # Turn backlight OFF
time.sleep(2) # Wait for two seconds
