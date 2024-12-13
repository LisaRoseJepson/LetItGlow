'''
Random colour generator (new colours beneath code)
'''

from machine import I2C, Pin
from lcd_api import LcdApi # lcd library
from pico_i2c_lcd import I2cLcd # lcd library
from dht20 import DHT20 # sensor library
import time
from neopixel import NeoPixel
import random

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

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    strand.fill((r, g, b))
    strand.write()
    lcd.putstr(str(r) + ", " + str(g) + ", " + str(b))
    print(f"({r}, {g}, {b})")
    
    time.sleep(3)
        
    lcd.clear()
    
'''
20, 207, 160 - icey blue
185, 50, 21 - rose
35, 163, 219 - bold icey blue
41, 62, 12 - lime green
81, 0, 164 - lilac
5, 100, 110 - blue icey blue
185, 25, 108 - bold pink
220, 142, 10 - amber
(27, 133, 236) - icey blue again
(8, 200, 177) - neon icey blue
(21, 100, 15) - apple green
(27, 236, 66) - jade green
(42, 217, 6) - neon green
(106, 14, 39) - neon pink

'''

