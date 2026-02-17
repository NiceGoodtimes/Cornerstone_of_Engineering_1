#imports
from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd
from time import sleep
import time

#variables
infrared_sensor = Pin(15, Pin.IN)
adc0 = ADC(26)

sections = 3
microseconds_per_minute = 60000000

last_value = infrared_sensor.value()
last_time = 0
current_rpm = 0


#functions

def check_edge():
    global last_value, last_time, current_rpm
    current_value = infrared_sensor.value()

    if current_value != last_value:
        last_value = current_value
        now = time.ticks_us()

        if last_time != 0:
            diff = time.ticks_diff(now, last_time)

            if diff > 0:
                rotation_time = diff * sections
                current_rpm = microseconds_per_minute / rotation_time

        last_time = now

#lcd setup
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.clear()
lcd.putstr("RPM: \nVoltage: ")
sleep(1)



#main
while True:
    check_edge()
    #voltage
    adc_value = adc0.read_u16()
    voltage = adc_value * (3.3 / 65535)
    #display
    lcd.move_to(0, 0)
    lcd.putstr("RPM: {:.2f}".format(current_rpm))
    lcd.move_to(0, 1)
    lcd.putstr("Voltage: {:.3f}".format(voltage))
    sleep(0.01)