'''
Random colour, random LED flash
'''

from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

# Set up pin for ring LED
ring = NeoPixel(Pin(2), 12)

# set all LEDs on ring to off
ring.fill((0,0,0))
ring.write()
time.sleep(1)

sleep = 0.1

# Random LEDs
while True:
            
    green = random.randint(0, 255)*10 # using 100 as less chance of choosing (0, 0, 0)
    red = random.randint(0, 255)*10
    blue = random.randint(0, 255)*10
        
    setting = (round(red / 10), round(green / 10), round(blue / 10)) # reducing intensity for James' eyes! :)
        
    rand_led = random.randint(0, 11)

    ring[rand_led] = setting
    ring.write() # Send the data to the ring
    time.sleep(sleep)
    ring.fill((0,0,0))


