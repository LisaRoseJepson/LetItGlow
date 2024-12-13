'''
String lights, random different colour twinkles with slider turning lights on/off
'''

from machine import Pin, ADC
import time
from neopixel import NeoPixel
import random

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# LED details
num_leds = 15
GPIO_number = 2

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Divide the analogue range by the number of LEDs
LEDdivision = (65535/num_leds)

# Colour list
# Define some GRB colour variables
white = 140,240,255 #White-ish!
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 175,255,150
orange = 223, 238, 105
pink = 150,150,200
purple = 100,40,255
iceblue = 25,150,200
unicorn = 150,175,255
bogey = 100, 215, 0

# Define colour
setting = iceblue

# Turn off all leds
strand.fill((0, 0, 0))
strand.write()

sleep = 0.1

while True:
    reading = round( (potentiometer.read_u16()) / LEDdivision )
    
    for led in range(reading):
        # Generate random RGB values
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        strand[led] = (r, g, b)
        
    # Set which LEDs should be OFF
    for ledoff in range ((reading),num_leds,1):
        strand[ledoff] = (0,0,0)
        
    strand.write()
    time.sleep(sleep)
        
        