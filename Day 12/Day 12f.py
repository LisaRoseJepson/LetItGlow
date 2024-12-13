'''
Change LEDs colours and print colour to LCD
'''

from machine import I2C, Pin
from lcd_api import LcdApi # lcd library
from pico_i2c_lcd import I2cLcd # lcd library
from dht20 import DHT20 # sensor library
import time
from neopixel import NeoPixel

# Define LCD/sensor I2C pins/BUS/address
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

# LED details
num_leds = 15
GPIO_number = 2

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Colours
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

mycolours ={
    "Red":(255,0,0),
    "Green":(0,255,0),
    "Blue":(0,0,255),
    "White":(255,255,255),
    "Yellow":(yellow),
    "Orange":(orange),
    "Pink":(pink),
    "Purple":(purple),
    "Iceblue":(iceblue),
    "Unicorn":(unicorn),
    "Bogey":(bogey)
}

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    for i in mycolours:
        lcd.putstr(i)
        strand.fill(mycolours[i])
        strand.write()
    
        time.sleep(1)
        
        lcd.clear()
    



