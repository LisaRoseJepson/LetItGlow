'''
Flashing block and on board LEDS
'''

# Imports
from machine import Pin
import time

#Pin setup
blockLED = Pin(14, Pin.OUT) # Set GPIO 14 as an output
greenLED = Pin(25, Pin.OUT)

# Program Start
while True:
    blockLED.value(1)
    greenLED.value(0)
    time.sleep(0.25)
    blockLED.value(1)
    greenLED.value(1)
    time.sleep(0.25)
    blockLED.value(0)
    greenLED.value(0)
    time.sleep(0.25)
    blockLED.value(0)
    greenLED.value(1)
    time.sleep(0.25)


