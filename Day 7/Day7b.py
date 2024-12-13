'''
Rainbow LEDs controlled with slider
'''

# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

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

    print(potentiometer.read_u16()) # Read the potentiometer value

    if potentiometer.read_u16() <= 10000:
        GRBled1.fill((red))
        GRBled1.write()
        GRBled2.fill((blue))
        GRBled2.write()
        
    elif potentiometer.read_u16() <= 20000:
        GRBled1.fill((yellow))
        GRBled1.write()
        GRBled2.fill((red))
        GRBled2.write()

    elif potentiometer.read_u16() <= 30000:
        GRBled1.fill((pink))
        GRBled1.write()
        GRBled2.fill((yellow))
        GRBled2.write()
        
    elif potentiometer.read_u16() <= 40000:
        GRBled1.fill((green))
        GRBled1.write()
        GRBled2.fill((pink))
        GRBled2.write()

    elif potentiometer.read_u16() <= 50000:
        GRBled1.fill((orange))
        GRBled1.write()
        GRBled2.fill((green))
        GRBled2.write()
        
    elif potentiometer.read_u16() <= 60000:
        GRBled1.fill((purple))
        GRBled1.write()
        GRBled2.fill((orange))
        GRBled2.write()
        
    else:
        GRBled1.fill((blue))
        GRBled1.write()
        GRBled2.fill((purple))
        GRBled2.write()
        
    time.sleep(0.3) # Short delay until the next reading
