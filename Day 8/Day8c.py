'''
Lighting up Stargate spinning
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
new_leds = leds[6:] + leds[:6]
setting = 0, 0, 10
sleep = 0.6

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
