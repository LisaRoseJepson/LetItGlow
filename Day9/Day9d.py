'''
Temperature and Humidity display (ring and bar with sensor) - full fill
'''

from machine import Pin, I2C
import time
from dht20 import DHT20
from neopixel import NeoPixel
import math

# Set up I2C pins
i2c1_sda = Pin(14)
i2c1_scl = Pin(15)

# Set up pin for ring LED
ring = NeoPixel(Pin(2), 12)

# Set up GPIOs 9-13 for bar graph LED
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Set up I2C
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)

# temperature-LED dictionary
temp_dict = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7, 16: 8, 17: 9, 18: 10, 19: 11}
hum_dict = {1: seg1, 2: seg2, 3: seg3, 4: seg4, 5: seg5}

# bar graph LED segments
segments = [seg1, seg2, seg3, seg4, seg5]

while True:
    
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    temp = round(measurements['t'])
    humidity = round(measurements['rh'])

    # turn bar graph LEDs off
    for segment in segments:
        segment.value(0)
    
    if temp not in temp_dict:
        
        pass
        print(f"*** Temperature {temp}°C is out of temperature range ***")

    else:
        ring.fill((0, 0, 0)) # turn all LEDs off
        ring.write()
        
        # Print the data
        print("------ Environment -------") # Heading
        print(f"Temperature:      {temp}°C")
        print(f"LED index:        {temp_dict[temp]}")
        
        temp_led = temp_dict[temp]
        value = 10
        
        if temp_led == 6:
            ring[temp_led] = (0, 50, 0)
        elif temp_led <= 11 and temp_led > 6:
            ring[6] = (0, 50, 0)
            for light in range(7, temp_led+1):
                ring[light] = (value, 0, 0)
                value += 10
        else:
            ring[6] = (0, 50, 0)
            for light in range(temp_led, 6):
                ring[light] = (0, 0, value)
                value += 10
        ring.write()
        
    hum_led = int(math.ceil(humidity/20)) # divide humidity % by 20 (for each of 5 LEDs) and round UP to select correct LED

    # light up all LEDs for that humidity e.g. 65% lights 1-4
    for seg in range(1, hum_led+1):
        current_seg = hum_dict[seg]
        current_seg.value(1)
    
    print(f"Humidty:          {humidity}%")
    print(f"LED index:        {hum_led}")
    print("\n")
    
    # Wait 5 seconds
    time.sleep(5)


