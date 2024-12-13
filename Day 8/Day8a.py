'''
Light up 4 ring LEDS
'''

from machine import Pin, ADC
from neopixel import NeoPixel
import time

# Set up pin for ring LED
ring = NeoPixel(Pin(2), 12)

# set all LEDs on ring to off
ring.fill((0,0,0))
ring.write()

# Select LEDs
# Set the RGB colour (blue)
ring[0] = (0,0,10)
ring[3] = (0,0,10)
ring[6] = (0,0,10)
ring[9] = (0,0,10)

# Send the data to the ring
ring.write()