#imports
from machine import Pin
import time

#pins
led = Pin(14, Pin.OUT)
sensor = Pin(15, Pin.IN)

#main
while True:
    print(sensor.value())
    time.sleep(0.01)
    if sensor.value() == 0:
        led.value(1)
    else:
        led.value(0)