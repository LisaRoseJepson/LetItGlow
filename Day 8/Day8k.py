'''
Set LEDs on ring to come on one by one, with random colour
'''

from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

# Set up pin for ring LED
ring = NeoPixel(Pin(2), 12)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# set all LEDs on ring to off
ring.fill((0,0,0))
ring.write()
time.sleep(1)

while True:

    reading = potentiometer.read_u16()
    
    if reading < 500:
        choice = 99
    elif reading < 5500:
        choice = 6
    elif reading < 11000:
        choice = 7
    elif reading < 16500:
        choice = 8
    elif reading < 22000:
        choice = 9
    elif reading < 27500:
        choice = 10
    elif reading < 33000:
        choice = 11
    elif reading < 38500:
        choice = 0
    elif reading < 44000:
        choice = 1
    elif reading < 49500:
        choice = 2
    elif reading < 55000:
        choice = 3
    elif reading < 60500:
        choice = 4
    else:
        choice = 5
        
    setting = (round(random.randint(0, 100)/10), round(random.randint(0, 100)/10), round(random.randint(0, 100)/10))

    if choice != 5 and choice != 99 and choice != 11:
        ring[choice] = setting
        ring[choice+1] = (0, 0, 0)
    elif choice == 11:
        ring[choice] = setting
        ring[0] = (0, 0, 0)        
    elif choice == 99:
        ring.fill((0, 0, 0))
    else:
        ring[choice] = setting
    ring.write()
