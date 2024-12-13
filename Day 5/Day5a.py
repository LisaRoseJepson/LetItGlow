'''
Turning on/off 5-switch
'''

from machine import Pin
import time

# Set up switch input pins
dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    
    # Switch 1
    if dip1.value() == 1:
        print("Switch 1: ON")
    else:
        print("Switch 1: OFF")

    # Switch 2
    if dip2.value() == 1:
        print("Switch 2: ON")
    else:
        print("Switch 2: OFF")
        
    # Switch 3
    if dip3.value() == 1:
        print("Switch 3: ON")
    else:
        print("Switch 3: OFF")

    # Switch 4
    if dip4.value() == 1:
        print("Switch 4: ON")
    else:
        print("Switch 4: OFF")

    # Switch 5
    if dip5.value() == 1:
        print("Switch 5: ON")
    else:
        print("Switch 5: OFF")
        
    # For each loop...
    print("-------------") # Print a divider
    time.sleep(5) # 5 second delay
