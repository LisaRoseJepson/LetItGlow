'''
Counting up and down with red and green button presses
'''

# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin number
# Set the pins as an input and use a pull down
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

 # Set GPIOs 14 & 25 as an outputs
redLED = Pin(14, Pin.OUT)
greenLED = Pin(25, Pin.OUT)

# Set count to 0
count = 0

while True: # Loop forever

    time.sleep(0.2) # Short delay
    redLED.value(0)
    greenLED.value(0)
    
    if redbutton.value() == 1: #If the red button is pressed
        print("Red button pressed")
        #redLED.value(0)
        redLED.toggle()
        count -= 1
        print(count)
    if greenbutton.value() == 1: #If the red button is pressed
        print("Green button pressed")
        count += 1
        print(count)
        #greenLED.value(0)
        greenLED.toggle()
