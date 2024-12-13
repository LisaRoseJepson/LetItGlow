'''
Check if all buttons aren't pressed before checking for another press
 - stops program detecting one press as multiple
'''

from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

state = 0

while True:
    
    time.sleep(0.1) # Short delay
    
    # If state = 0, allow checking for keypress
    if state == 0:
    
        if key1.value() == 1:
            print("Button 1")
            state = 1
            
        elif key2.value() == 1:
            print("Button 2")
            state = 1
            
        elif key3.value() == 1:
            print("Button 3")
            state = 1
            
        elif key4.value() == 1:
            print("Button 4")
            state = 1
    
    # Only runs if state = 1 AND all keys are LOW
    elif state == 1 and key1.value() == key2.value() == key3.value() == key4.value() == 0:
        
        state = 0
