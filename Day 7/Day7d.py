# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1) # GRB LED1
GRBled2 = NeoPixel(Pin(5), 1) # GRB LED2

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define some GRB colour variables
white = 240,140,255 #White-ish!
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

while True: # Loop forever
    
    print("Slider Reading: ", potentiometer.read_u16()) # Read the potentiometer value
    
    reading = potentiometer.read_u16()
    
    time_delay = reading / 65535
    
    print("Delay: ", time_delay)
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    GRBled1.fill((g, r, b))
    GRBled1.write()
    GRBled2.fill((r, b, g))
    GRBled2.write()
    
    time.sleep(time_delay) # Short delay until the next reading