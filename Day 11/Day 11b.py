'''
Using keypad to select colours
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

# LED details
num_leds = 15
GPIO_number = 2

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# LED index list
ledindex = list(range(0, 15))

# Colour variables
off = 0,0,0
red = 255,0,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255
yellow = 255,255,0
pink = 255,0,255
aqua = 0,255,255

# Define function
def pattern(colour1, colour2):
    
    for led in ledindex:
        if led % 2 == 0: # if even number
            strand[led] = (colour1)
        else: # if odd number
            strand[led] = (colour2)
            
    strand.write()
    
# Turn LEDs off
pattern(off, off)

while True:

    if key1.value() == 1:
        pattern(red, green)
    elif key2.value() == 1:
        pattern(blue, white)
    elif key3.value() == 1:
        pattern(aqua, pink)
    elif key4.value() == 1:
        pattern(off, off)
    else:
        print("Press a key!")
    
    sleep(1)
        
