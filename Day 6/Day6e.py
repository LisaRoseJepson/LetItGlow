'''
Fading LEDs in/out
'''

# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1) # GRB LED1
GRBled2 = NeoPixel(Pin(5), 1) # GRB LED2

while True:
    
    # First LED fades in
    for i in range(255):
        
        GRBled1.fill((i,0,0))

        GRBled1.write()
        
        time.sleep(0.005)
    
    #Turn off the first LED
    GRBled1.fill((0,0,0)) # All zero = no light!
    GRBled1.write()
    
    # Second LED fades out (using reversed)
    for i in reversed (range(255)):
        
        GRBled2.fill((i,0,0))

        GRBled2.write()
        
        time.sleep(0.005)