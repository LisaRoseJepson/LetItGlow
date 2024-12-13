'''
Attempt 1 of 2 - Atlantis Stargate
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

leds = list(range(12))
new_leds = leds[6:] + leds[:6]
setting = 0, 0, 10
sleep = 0.6

glyphs = [7, 8, 9, 3, 4, 5]
for glyph in glyphs:
    ring[glyph] = setting
    ring.write()
    time.sleep(sleep)

glyphs2 = [0, 1, 2, 6, 10, 11]
for glyph in glyphs2:
    ring[glyph] = setting
    ring.write()
    
time.sleep(sleep)
ring.fill((0, 0, 0))

# Stargate
while True:
    if sleep > 0.1:
        sleep -= 0.1
        print(sleep)
    else:
        sleep = 0.1
        
    for led in new_leds:
        ring[led] = (setting)
        ring.write() # Send the data to the ring
        time.sleep(sleep)
        ring.fill((0,0,0))

