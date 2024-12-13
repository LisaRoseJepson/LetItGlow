'''
Lighting entire ring at once with colour changes on each cycle
'''

# Imports
from machine import Pin
from neopixel import NeoPixel
import time
import random

# Define the strip pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)
        
while True:
    
    # Create random RGB values
    r = random.randint(0,100)
    g = random.randint(0,100)
    b = random.randint(0,100)
    
    for i in range(12):
        
        # Light each LED a random colour
        ring[i] = (r,g,b)
        ring.write()
        
        # Show the LED for this long
#        time.sleep(0.05)
        
        #Clear the ring at the end of each loop
#        ring.fill((0,0,0))
#        ring.write()
    time.sleep(0.5)
