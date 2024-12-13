'''
Light up GRB LED
'''

# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1) # GRB LED

# Set to blue (highest intensity)
# GRBled.fill((0,0,255))

# Set up variables to set colour
red = 0, 255, 0
green = 255, 0, 0
blue = 0, 0, 255

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

# Set to colour
GRBled.fill((white))

# Write the data to the LED
GRBled.write()