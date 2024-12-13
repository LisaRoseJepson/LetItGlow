'''
Using switches to select light patterns
1) on one by one, off one by one
2) Knightrider!
'''

from machine import Pin
import time
import random

# Set up switch input pins
dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Set up LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]

# turn on one by one, then off one by one
def myfunction1():
    r = random.randint(0,4)
    segments[r].value(1)
    time.sleep(1)
    segments[r].value(0)
        
def myfunction2():
# Knightrider! Turn them on left then right
    for segment in segments:
        segment.value(1)
        time.sleep(0.08)
        segment.value(0)
        
    for segment in reversed(segments):
        segment.value(1)
        time.sleep(0.08)
        segment.value(0)

while True:
    
    # Switch 1
    if dip1.value() == 1 or dip2.value() == 1:
        myfunction1()

    # Switch 2
    elif dip3.value() == 1 or dip4.value() == 1:
        myfunction2()