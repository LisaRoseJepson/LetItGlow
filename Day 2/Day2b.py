'''
Lighing block LED and on board LED
'''

from machine import Pin

green = Pin(25, Pin.OUT)
red = Pin(14, Pin.OUT)

green.value(1)
red.value(1)

print("Both LEDs ON!")
