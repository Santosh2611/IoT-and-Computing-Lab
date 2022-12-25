from sense_hat import SenseHat # Python module to control the Raspberry Pi Sense HAT
sense = SenseHat()
sense.clear() # No arguments defaults to OFF

from time import sleep # Handle time-related tasks

# Initialize the colours:-
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

# Humidity Sensor Programming:-
humidity = sense.get_humidity() # Gets the percentage of relative humidity from the humidity sensor.
print("Relative Humidity: " + str(round(humidity, 2)) + " %")

# Pressure Sensor Programming:-
pressure = sense.get_pressure() # Gets the current pressure in Millibars from the pressure sensor.
print("Current Pressure: " + str(round(pressure, 2)) + " millibars")

# Temperature Sensor Programming:-
temperature = sense.get_temperature()
print("Temperature: " + str(round(temperature, 2)) + " degree(s)")

# Print Local Time:-
seconds = time.time() # Return the time in seconds since the epoch as a floating point number. 
local_time = time.ctime(seconds) # Convert a time expressed in seconds since the epoch to a string of a form:
                                 # 'Sun Jun 20 23:21:05 1993' representing local time.
print("Local Time: " + str(local_time))

# Temperature Controller using SenseHAT:-
if (temperature>34):
    sense.show_message("Temperature Limit Crossed!",
                       scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                       text_colour = green, # Text Colour
                       back_colour = red) # Background Colour
    print("Temperature Limit Crossed!")
sense.clear() # No arguments defaults to OFF

# Accelerometer Sensor Programming
:-
accel_only = sense.get_accelerometer() # Calls set_imu_config to disable the magnetometer and gyroscope;
                                       # Then, gets the current orientation from the accelerometer only.
print("Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}".format(**accel_only))

sense.show_message("Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}".format(**accel_only),
                   scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                   text_colour = yellow, # Text Colour
                   back_colour = blue) # Background Colour

# Acceleration Detector using Accelerometer:-
raw = sense.get_accelerometer_raw() # Gets the raw x, y and z axis accelerometer data.
print("x: {x}, y: {y}, z: {z}".format(**raw))

sense.show_message("x: {x}, y: {y}, z: {z}".format(**raw),
                   scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                   text_colour = yellow, # Text Colour
                   back_colour = blue) # Background Colour

# Acceleration Detector along with Direction Detection using Accelerometer:-
if (raw["z"]>0.975):
    sense.show_message("Z-Axis Limit Crossed!",
                       scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                       text_colour = green, # Text Colour
                       back_colour = red) # Background Colour
    print("Z-Axis Limit Crossed!")
sense.clear() # No arguments defaults to OFF

# Datalogger for Weather Station using SenseHat:
with open('Datalogger_Weather_Station', 'w') as f:
    while True:
        
        pressure = sense.get_pressure() # Gets the current pressure in Millibars from the pressure sensor.            
        humidity = sense.get_humidity() # Gets the percentage of relative humidity from the humidity sensor.            
        temperature = sense.get_temperature()

        seconds = time.time() # Return the time in seconds since the epoch as a floating point number. 
        local_time = time.ctime(seconds) # Convert a time expressed in seconds since the epoch to a string of a form:
                                         #'Sun Jun 20 23:21:05 1993' representing local time.
        
        print_message = str("Current Pressure: " + str(pressure) +
                            "Relative Humidity: " + str(humidity) +
                            "Temperature (Degrees): " + str(temperature) +
                            "Local Time: " + str(local_time))
        
        sense.show_message(print_message,
                       scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                       text_colour = green, # Text Colour
                       back_colour = red) # Background Colour

        f.writelines(print_message)
        f.write("\n")
        sense.clear() # No arguments defaults to OFF

# Assignment: To implement a multiparameter display device which will display the
#             current temperature, humidity and pressure on the LED matrix in 
#             SenseHAT when the middle button of the joystick is pressed.
while True:
    for event in sense.stick.get_events(): # Returns a list of InputEvent tuples representing all events that have occurred since the last call to get_events or wait_for_event
        if (event.direction == "middle" and event.action == "held"):
            
            sense.show_message("Current Pressure: {} Relative Humidity: {} Temperature: {}"
                               .format(pressure, humidity, temperature),
                               scroll_speed = 0.005, # Control Scroll Speed; Greater speed implies slower scroll time
                               text_colour = yellow, # Text Colour
                               back_colour = blue) # Background Colour

        sense.clear() # No arguments defaults to OFF
        break

