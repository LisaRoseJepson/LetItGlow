'''
Turning block LED on
'''

from machine import Pin

blockLED = Pin(14, Pin.OUT)

blockLED.value(1)

print("Block LED on!")
