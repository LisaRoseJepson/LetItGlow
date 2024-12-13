'''
Pulsing white light on colour string
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

# Colour list
# Define some GRB colour variables
white = 140,240,255 #White-ish!
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 175,255,150
orange = 223, 238, 105
pink = 150,150,200
purple = 100,40,255
iceblue = 25,150,200
unicorn = 150,175,255
bogey = 100, 215, 0

# Define colour
setting = iceblue

sleep = 0.1

while True:
    strand.fill((setting)) # set all LEDs on strand to low intensity blue
    strand.write()
    time.sleep(0.5)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (i, i, i)
            strand.write()
        strand[led] = (setting)
        strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (i, i, i)
            strand.write()
        strand[led] = (setting)
        strand.write()