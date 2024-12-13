'''
Check if PIN number is correct and print presents list (Team Jepson version)
'''

from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Set up lists
pin_num = [2, 4, 3, 1]
user_entry = []
presents = ["Pico", "Pi", "Books", "Run things", "Random parkrun branded shizzle"]
correct_entry = False

state = 0

# Append function
def appendkey(key):
    
    global state
    user_entry.append(key)
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

while correct_entry == False:
    
    time.sleep(0.1) # Short delay
    
    # If state = 0 and less than 4 digits entered, allow checking for keypress
    if state == 0 and len(user_entry) < 4:
    
        if key1.value() == 1:
            appendkey(1)
            
        elif key2.value() == 1:
            appendkey(2)
            
        elif key3.value() == 1:
            appendkey(3)
            
        elif key4.value() == 1:
            appendkey(4)
    
    # Only runs if state = 1 and less than 4 digits entered AND all keys are LOW
    elif state == 1 and len(user_entry) <4 and key1.value() == key2.value() == key3.value() == key4.value() == 0:
        
        state = 0
        
    elif len(user_entry) == 4: # if 4 digits entered
        
        # compare pin_num with user_entry
        
        if pin_num == user_entry:
            
            for present in presents:
                print(present)
                
            correct_entry = True
            
        else:
            print("\nWrong PIN! Try again...")
            user_entry = []

    else:
        pass