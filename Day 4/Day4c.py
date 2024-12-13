'''
Lighting up bar graph LED - Knightrider lights
'''

# Imports
from machine import Pin
import time

# Set up GPIOs 9-13
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]
    
# Knightrider! Turn them on left then right
while True:
    for segment in segments:
        segment.value(1)
        time.sleep(0.08)
        segment.value(0)
        
    for segment in reversed(segments):
        segment.value(1)
        time.sleep(0.08)
        segment.value(0)


