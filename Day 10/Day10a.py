'''
Red string on/off
'''

from machine import Pin, ADC
import time
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define the strand pin number (2) and number of LEDs (15)
strand = NeoPixel(Pin(2), 15)

# Fill with red for 10 seconds
strand.fill((50,0,0))
strand.write()
time.sleep(10)

# Turn off
strand.fill((0,0,0))
strand.write()