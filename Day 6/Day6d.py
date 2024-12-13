'''
Colour cycling and chasing colours through both lights
'''

# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1) # GRB LED1
GRBled2 = NeoPixel(Pin(5), 1) # GRB LED2


# Define some GRB colour variables
white = 240,140,255 #White-ish!
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

colour_list = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

# Loop through all colours
while True:
    for colour in colour_list:
        GRBled1.fill((colour)) # Set colour
        GRBled1.write() # Write the data to the LED
        time.sleep(0.25)
        GRBled1.fill((0, 0, 0)) # turn off LED1
        GRBled1.write() # Write the data to the LED
        GRBled2.fill((colour)) # Set colour
        GRBled2.write() # Write the data to the LED
        time.sleep(0.25)
        GRBled2.fill((0, 0, 0)) # turn off LED1
        GRBled2.write() # Write the data to the LED



        
    





