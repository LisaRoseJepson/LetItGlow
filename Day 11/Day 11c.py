'''
Using keypad to select flashing rates
'''

# Imports
from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Set up our LED
blockLED = Pin(6, Pin.OUT)

# Create the flash variable
flash = 0

# Create our simple function
def program1():

    blockLED.value(1) # LED ON
    time.sleep(flash)
    
    blockLED.value(0) # LED off
    time.sleep(flash)
        
while True:
    
    while key1.value() == 1:
        
        flash = 1
        program1()
        
    while key2.value() == 1:
        
        flash = 0.5
        program1()

    while key3.value() == 1:
        
        flash = 0.1
        program1()
        
    while key4.value() == 1:
        
        flash = 0.05
        program1()

