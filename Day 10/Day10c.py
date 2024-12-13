'''
Green red bounce on blue
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

# set all LEDs on strand to low intensity blue
strand.fill((0,0,5))
strand.write()
time.sleep(1)

sleep = 0.1

while True:
    strand.fill((0,0,5))
    strand.write()
    time.sleep(0.5)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (0, i, 0)
            strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (i, 0, 0)
            strand.write()