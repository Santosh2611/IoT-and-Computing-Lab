# Assignment - There is a digital board installed in a smart restaurant.
#              Read 'n' numbers of today's special food items as input through keyboard.
#              Scroll through the read foods one by one on LCD for customer's view.    

import time # Provides various time-related functions
import board # Implements a general-purpose board structure which has the functionality needed for a range of purposes
import digitalio # Contains classes to provide access to basic digital IO
import adafruit_character_lcd.character_lcd as characterlcd # Module for interfacing with monochromatic character LCDs

# Modify this if you have a different sized character LCD: -
lcd_columns = 16; lcd_rows = 2

# Metro M0/M4 Pin Config: -
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_backlight = digitalio.DigitalInOut(board.D13)

# Initialise the LCD Class: -
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.backlight = True # Turn backlight ON
lcd.message = "Welcome!" # Print a message
time.sleep(5) # Wait for five seconds
lcd.clear() # Clear my LCD

n = int(input("Enter n value: "))
food_items = []   

for i in range(n):
    
    item = str(input("Enter food item: "))
    food_items.append(item)
    time.sleep(1) # Wait for a second
    print(food_items[i])
    
    # Scroll message to the left: - 
    for j in range(len(food_items[i])):
        time.sleep(0.5) # Wait for half a second
        lcd.move_left() # Moves displayed text left one column
    lcd.clear() # Clear my LCD

time.sleep(3) # Wait for three seconds
lcd.backlight = False # Turn backlight OFF
time.sleep(2) # Wait for two seconds
