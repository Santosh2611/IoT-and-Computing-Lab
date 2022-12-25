# Hello World Display as LCD (GPIO)

# sudo pip install adafruit-circuitpython-charlcd
import time # Provides various time-related functions
import board # Implements a general-purpose board structure which has the functionality needed for a range of purposes
import digitalio # Contains classes to provide access to basic digital IO

# # import Adafruit_CharLCD as LCD # Library to drive character LCD display and plate.
import adafruit_character_lcd.character_lcd as characterlcd # Module for interfacing with monochromatic character LCDs

# Modify this if you have a different sized character LCD:-
lcd_columns = 16; lcd_rows = 2

# # Raspberry Pi pin configuration: -
# # rs = 26 # Reset data line
# # en = 19 # Enable data line
# # d4 = 13 # Data line 4
# # d5 = 10 # Data line 5
# # d6 = 5 # Data line 6
# # d7 = 21 # Data line 7

# Metro M0/M4 Pin Config:-
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_backlight = digitalio.DigitalInOut(board.D13)

# Initialise the LCD Class:-

# # backlight = 2 # Contrast - Backlight Pin
# # rows = 2 # Define number of rows of my LCD
# # cols = 16 # Define number of columns in a row
# # mylcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, cols, rows, backlight)
# # 
# # mylcd.backlight = True # mylcd.backlight(True)
# # mylcd.cursor = True # Enable cursor visible
# # mylcd.bink = True # True for blinking cursor; False for stop blinking
# # mylcd.message("Hello World !!! \n LCD Test") # Send message to my LCD
# # 
# # time.sleep(5) # Delay for 5 seconds
# # mylcd.clear() # Clear my LCD and remove
# # mytext = raw_input("Enter text to be displayed: ") # Read user input text
# # 
# # mylcd.message(mytext) # Send the read text to my LCD
# # time.sleep(5) # Delay for 5 seconds
# # mylcd.clear() # Clear my LCD
# # mylcd.backlight = False # Turn backlight OFF

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.backlight = True # Turn backlight ON
lcd.message = "Hello\nCircuitPython" # Print a two line message
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD
