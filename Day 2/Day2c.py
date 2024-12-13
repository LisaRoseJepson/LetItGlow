'''
Flashing block LED
'''

# Imports
from machine import Pin
import time

#Pin setup
blockLED = Pin(14, Pin.OUT) # Set GPIO 14 as an output

# Program Start
for light in range(10):
    blockLED.value(1)
    time.sleep(0.25)
    blockLED.value(0)
    time.sleep(0.25)


