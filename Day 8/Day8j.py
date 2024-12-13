'''
Attempt 2 of 2 (finished) - Atlantis Stargate
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

seq1 = [6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8]
glyph1 = 7

seq2 = [8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6]
glyph2 = 8

seq3 = [6, 5, 4, 3, 2, 1, 0, 11, 10]
glyph3 = 9

seq4 = [10, 11, 0, 1, 2, 3, 4, 5, 6, 10, 11, 0, 1, 2]
glyph4 = 3

seq5 = [2, 1, 0, 11, 10, 6, 5]
glyph5 = 4

seq6 = [5, 6, 10, 11, 0, 1, 2]
glyph6 = 5

seq7 = [2, 1, 0, 11, 10]
glyph7 = [6, 0, 1, 2, 10, 11]

# Atlantis Stargate
for glyph in seq1:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph1] = setting
ring.write()

for glyph in seq2:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph2] = setting
ring.write()

for glyph in seq3:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph3] = setting
ring.write()

for glyph in seq4:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph4] = setting
ring.write()

for glyph in seq5:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph5] = setting
ring.write()

for glyph in seq6:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
ring[glyph6] = setting
ring.write()

for glyph in seq7:
    ring[glyph] = setting
    ring.write()
    time.sleep(0.1)
    ring[glyph] = 0, 0, 0
    
for glyph in glyph7:
    ring[glyph] = setting
    ring.write()


