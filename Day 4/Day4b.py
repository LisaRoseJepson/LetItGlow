'''
Lighting up bar graph LED segment by segment (using for loops)
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

# turn on segments one by one, then turn all off
segments = [seg1, seg2, seg3, seg4, seg5]

for segment in segments:
    segment.value(1)
    time.sleep(1)

for segment in segments:
    segment.value(0)
    



