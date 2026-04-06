"""
EQUATIONS
    Power = Voltage * Current

NOTES
    - Voltage will be 1/10 of actual, coming through divider
    - two voltage sensors and resistor,
    measuring difference over the sensors,

    (v1-v2)/r = i
"""

"""
IMPORTS
"""
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep

"""
VARIABLES
"""
typing_delay = 0.1
text_output = "No Text Provided"
lcd_data = 0
lcd_clock = 1

"""
PIN ASSIGNMENTS
"""
i2c = I2C(0, sda=Pin(lcd_data), scl=Pin(lcd_clock), freq=400000)   #Data pin 0, clock pin 1
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

"""
FUNCTIONS
"""
#displays each character incrementally on the screen
def text_printer(display, text):
    global typing_delay
    for i in text:
        display.putstr(i)
        sleep(typing_delay)

"""
MAIN
"""
while True:
    #cursor startup
    lcd.show_cursor()
    lcd.blink_cursor_on()
    #display desired text
    text_printer(lcd, text_output)
    #pause
    sleep(3)
    #cursor end
    lcd.blink_cursor_off()
    lcd.hide_cursor()
    #reset the screen (refresh rate)
    sleep(1)
    lcd.clear()