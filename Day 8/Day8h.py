'''
Random colour colour chase - colour changes each cycle
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
setting = (0, 0, 0)
old_setting = setting
sleep = 0.1

# Colour chasing LEDs
while True:
      
    while old_setting == setting or setting == (0, 0, 0):
        green = random.randint(0, 1)
        red = random.randint(0, 1)
        blue = random.randint(0, 1)
        
        setting = (red*10, green*10, blue*10)
            
    old_setting = setting
    
    for led in new_leds:
        ring[led] = setting
        ring[led-1] = setting
        ring[led-2] = setting
        ring.write() # Send the data to the ring
        time.sleep(sleep)
        ring.fill((0,0,0))



