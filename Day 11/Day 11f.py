'''
Check if PIN number is correct and print presents list (Pi Hut version)
'''

from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Set up our LED
blockLED = Pin(6, Pin.OUT)

# Create list of presents
presents = ["Train set","Furby","Boomerang","YoYo"]

# Set your passcode in a list
passcode = [1,2,3,4]

# Empty list for the entered password
userentry = []

# Create state variable
state = 0

# Create keypress variable
key = 0

# Append function
def appendkey():
    
    global state
    userentry.append(key)
    print("*", end="")
    state = 1

# Delay + print function
def myprint(mytext):
    print(mytext)
    time.sleep(0.5)
    
## Start our program ##
print("") # Empty line
print("Welcome to the Secret Present List system")
time.sleep(1)
print("Enter the passcode to continue: ", end="")

# While userentry length is less than 4
while len(userentry) < 4:
    
    time.sleep(0.1)
    
    if state == 0:

        if key1.value() == 1:
            key = 1
            appendkey()

        elif key2.value() == 1:
            key = 2
            appendkey()
            
        elif key3.value() == 1:
            key = 3
            appendkey()
        
        elif key4.value() == 1:
            key = 4
            appendkey()
    
    # If state is 1 and all keys are LOW
    elif state == 1 and key1.value() == key2.value() == key3.value() == key4.value() == 0:
        
        state = 0
        
    else:
        pass # Do nothing

# Program only gets this far if userentry is 4 characters long

# If the passcode is correct
if userentry == passcode:
    
    blockLED.value(1) # LED on
    
    print("\n") #Empty newline
    print("----------------------")
    print("*** ACCESS GRANTED ***")
    myprint("----------------------")
    myprint("Secret present list:")
    
    # Print each present from our list
    for i in presents:
        myprint(i)

    myprint("----------------------")
    
    blockLED.value(0) # LED off

# If the keyed code is incorrect
else:

    myprint("\n------------------")
    myprint("INCORRECT PASSCODE")
    myprint("ACCESS DENIED")
    time.sleep(1)