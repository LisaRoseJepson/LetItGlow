'''
Randomly choosing LEDS until one has been lit 10 times
'''

# Imports
from machine import Pin
import time
import random

# Set up GPIOs 9-13
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# set up vars
segments = [seg1, seg2, seg3, seg4, seg5]
LED1 = 0
LED2 = 0
LED3 = 0
LED4 = 0
LED5 = 0

# turn off all LEDs
for segment in segments:
    segment.value(0)
    
# Random LEDs
while True:
    r = random.randint(0,4)
    segments[r].value(1)
    time.sleep(1)
    segments[r].value(0)
    
    # count number of times each LED lights
    if r == 0:
        LED1 += 1
        print("LED1: ", LED1)
    elif r == 1:
        LED2 += 1
        print("LED2: ", LED2)
    elif r == 2:
        LED3 += 1
        print("LED3: ", LED3)
    elif r == 3:
        LED4 += 1
        print("LED4: ", LED4)
    else:
        LED5 += 1
        print("LED5: ", LED5)
        
    # when one LEDs lights 10 times, flash and display counts    
    if LED1 == 10 or LED2 == 10 or LED3 == 10 or LED4 == 10 or LED5 == 10:
        
        print("LED", r+1, " got to 10!!!")
        
        mylist = [("LED1", LED1), ("LED2", LED2), ("LED3", LED3), ("LED4", LED4), ("LED5", LED5)]
        mylistsorted = sorted(mylist, key=lambda x: x[1])
        
        # display counts
        for item in reversed(mylistsorted):
            print(item[0], ": ", item[1])
        
        # flash
        for i in range(10):
            segments[r].value(1)
            time.sleep(0.25)
            segments[r].value(0)
            time.sleep(0.25)
            
        break