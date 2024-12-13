'''
Single blue bounce
'''

from machine import Pin, ADC
import time
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# LED details
num_leds = 15
GPIO_number = 2

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Define colour
setting = 0, 0, 50

# set all LEDs on strand to off
strand.fill((0,0,0))
strand.write()
time.sleep(1)

sleep = 0.1

# Bouncing LEDs
while True:
        
    for led in range(num_leds):
        strand[led] = (setting)
        strand.write() # Send the data to the strand
        time.sleep(sleep)
        strand.fill((0,0,0))

    for led in reversed(range(num_leds)):
        strand[led] = (setting)
        strand.write() # Send the data to the strand
        time.sleep(sleep)
        strand.fill((0,0,0))