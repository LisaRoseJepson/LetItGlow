'''
Lighting up 4 LEDs on ring
'''

from machine import Pin, ADC
from neopixel import NeoPixel
import time

# Set up pin for ring LED
ring = NeoPixel(Pin(2), 12)

# set all LEDs on ring to off
ring.fill((0,0,0))
ring.write()
time.sleep(1)

leds = [0, 3, 6, 9]
setting = 0, 10, 0

# Set LEDs
for led in leds:
    ring[led] = (setting)
    ring.write() # Send the data to the ring
    time.sleep(1)



