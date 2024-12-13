'''
Bouncing LEDs on ring
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

leds = list(range(12))
new_leds = leds[6:] + leds[:6] + leds[6:7]
setting = 10, 0, 0
sleep = 0.1

# Bouncing LEDs
while True:
        
    for led in new_leds:
        ring[led] = (setting)
        ring.write() # Send the data to the ring
        time.sleep(sleep)
        ring.fill((0,0,0))

    for led in reversed(new_leds):
        ring[led] = (setting)
        ring.write() # Send the data to the ring
        time.sleep(sleep)
        ring.fill((0,0,0))