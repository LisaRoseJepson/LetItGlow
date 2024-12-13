'''
Using two buttons to count up and down on bar graph LED
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

# Set up buttons
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# tSet up variables
count = -1
segments = [seg1, seg2, seg3, seg4, seg5]

for segment in segments:
    segment.value(0)

# Random LEDs
while True:
    
    time.sleep(0.2)
    
    if greenbutton.value() == 1:
        if count == 4:
            pass
        else:
            count += 1
            segments[count].value(1)
            print("Count is: ", count+1)
            
            if count == 4:
                print("Well done!!!")
        
    if redbutton.value() == 1:
        if count == -1:
            pass
        else:
            segments[count].value(0)
            count -= 1         
            print("Count is: ", count+1)



        



