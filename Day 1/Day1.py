'''
Turning on board light on and off
'''

from machine import Pin
onboardLED = Pin(25, Pin.OUT)
onboardLED.value(0)

print("Light off!!!")