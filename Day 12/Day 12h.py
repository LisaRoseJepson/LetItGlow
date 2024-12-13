'''
Scrolling code example
'''

from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time

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
  
def ScrollLeft(text):
    
    # Adds 16 blank spaces after our string
    text = text + (16 * " ")
                    
    while True:
        
        # Always start each loop at 0,0
        lcd.move_to(0, 0)
        
        # Show the first 16 characters of the string
        lcd.putstr(text[:16])
        
        # Scroll speed delay
        time.sleep(0.5)
        
        # Updates 'text' before the next loop
        # text[1:] removes the first character
        # + text[0] adds the first character to the end
        text = text[1:] + text[0]
        
        print(text)

# Run our function
ScrollLeft("ALL YOUR BASE ARE BELONG TO ME!")
