#imports
from machine import Pin
import time

#variables
n_cycle = 0

#functions
def changed(x, n):
    n = n%2
    values = []
    values[n] = x
    average = (values[0] + values[1])/2
    if average != values[n]:
        return True
    else:
        return False

#pins
output = Pin(14, Pin.OUT)
infared_sensor = Pin(15, Pin.IN)

#main
while True:
    n_cycle =+ 1

    print(infared_sensor.value())
    time.sleep(0.01)
    if infared_sensor.value() == 0:
        output.value(1)
    else:
        output.value(0)

