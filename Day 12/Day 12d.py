'''
Display current temperature and humidity
'''

from machine import I2C, Pin
from lcd_api import LcdApi # lcd library
from pico_i2c_lcd import I2cLcd # lcd library
from dht20 import DHT20 # sensor library
import time

# Define LCD/sensor I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27
TEMP_ADDR = 0x38

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Set up temperature sensor I2C
tempi2c = I2C(I2C_BUS, sda=SDA, scl=SCL)
dht20 = DHT20(TEMP_ADDR, tempi2c)

lcd.putstr("Temp:")
lcd.move_to(0, 1)
lcd.putstr("Humidity:")

while True:
    
    temperature = round(dht20.measurements["t"], 1)
    humidity = round(dht20.measurements["rh"], 1)
    
    print(f"Temp: {temperature}, Humidity: {humidity}")
    
    lcd.move_to(11, 0)
    lcd.putstr(str(temperature) + "C")
    lcd.move_to(11, 1)
    lcd.putstr(str(humidity) + "%")
    
    time.sleep(5)
    

