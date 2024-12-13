'''
Lighting up bar graph LED segment by segment
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

# turn on segments 1 by 1, then turn all off
seg1.value(1)
time.sleep(1)
seg2.value(1)
time.sleep(1)
seg3.value(1)
time.sleep(1)
seg4.value(1)
time.sleep(1)
seg5.value(1)
time.sleep(1)
seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)