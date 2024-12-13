'''
Testing PIN pad
'''

# Imports
from machine import Pin
from neopixel import NeoPixel
from time import sleep

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if key1.value() == 1:
        print("Key 1 pressed")
    elif key2.value() == 1:
        print("Key 2 pressed")
    elif key3.value() == 1:
        print("Key 3 pressed")
    elif key4.value() == 1:
        print("Key 4 pressed")
    else:
        print("Press a key!")
    
    sleep(1)
        