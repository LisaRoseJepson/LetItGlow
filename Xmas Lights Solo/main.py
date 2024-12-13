'''
Alternative red green flashing
'''

from machine import Pin, ADC, I2C
import time
from neopixel import NeoPixel
import random
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Set up our button names and GPIO pin number
# Set the pins as an input and use a pull down
redbutton = Pin(7, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(6, Pin.IN, Pin.PULL_DOWN)

# LED details
num_leds = 15
GPIO_number = 2

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Colour list
# Define some GRB colour variables
white = 140,240,255 #White-ish!
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 175,255,150
orange = 223, 238, 105
pink = 150,150,200
purple = 100,40,255
iceblue = 25,150,200
unicorn = 150,175,255
bogey = 100, 215, 0
iceiceblue = 20, 207, 160
rose = 185, 50, 21
boldiceblue = 35, 163, 219
limegreen = 41, 62, 12
lilac = 81, 0, 164
blueiceblue = 5, 100, 110
boldpink = 185, 25, 108
amber = 220, 142, 10
iceblueagain = 27, 133, 236
neonblue = 8, 200, 177
applegreen = 21, 100, 15
jadegreen = 27, 236, 66
neongreen = 42, 217, 6
neonpink = 106, 14, 39

speed = 0.5

num_colours = 7

def pattern1(colour1 = green, colour2 = red, speed = 0.5):
    # Two colour chasing    
    for led in range(num_leds):
        if led%2 == 0:
            strand[led] = (colour1)
            strand.write()
        else:
            strand[led] = (colour2)
            strand.write()
    
    time.sleep(speed)
    
    for led in range(num_leds):
        if led%2 != 0:
            strand[led] = (colour1)
            strand.write()
        else:
            strand[led] = (colour2)
            strand.write()
            
    time.sleep(speed)

def pattern2(speed):
    # random twinkles
    for led in range(num_leds):
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        strand[led] = (r, g, b)
        strand.write()
        
    time.sleep(speed)
    
def pattern3(speed):
    # pulse iceblue on blue
    strand.fill((blue)) # set all LEDs on strand to low intensity blue
    strand.write()
    time.sleep(speed)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (iceblue)
            strand.write()
        strand[led] = (blue)
        strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (iceblue)
            strand.write()
        strand[led] = (blue)
        strand.write()
        
def pattern4(speed):
    
    strand.fill((0,0,5))
    strand.write()
    time.sleep(speed)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (0, i, 0)
            strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (i, 0, 0)
            strand.write()

while True:
    
    # Take potentiometer reading for colour selection
    
    colour = potentiometer.read_u16()/65535*num_colours
    
    if redbutton.value() == 1: #If the red button is pressed
        speed += 0.25
        print("Red")
        print(f"Interval: {speed}")
    if greenbutton.value() == 1: #If the green button is pressed
        speed -= 0.25
        print("Green")
        print(f"Interval: {speed}")
        
    if speed > 2:
        speed = 2
    elif speed < 0.25:
        speed = 0.25
    else:
        speed = speed
        
    if colour <= 1:
        lcd.move_to(0, 0)
        lcd.putstr("Red Green Chase")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern1(red, green, speed)
    elif colour <= 2:
        lcd.move_to(0, 0)
        lcd.putstr("Green Blue Chase")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern1(neongreen, neonblue, speed)
    elif colour <= 3:
        lcd.move_to(0, 0)
        lcd.putstr("Rose Lilac Chase")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern1(rose, lilac, speed)
    elif colour <= 4:
        lcd.move_to(0, 0)
        lcd.putstr("Jade Purp Chase ")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern1(jadegreen, purple, speed)
    elif colour <= 5:
        lcd.move_to(0, 0)
        lcd.putstr("Twinkles         ")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern2(speed)
    elif colour <= 6:
        lcd.move_to(0, 0)
        lcd.putstr("Blue Pulse      ")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern3(speed)
    else:
        lcd.move_to(0, 0)
        lcd.putstr("RGB Bounce      ")
        lcd.move_to(0, 1)
        lcd.putstr("Interval: " + str(speed) + " ")
        pattern4(speed)
        
