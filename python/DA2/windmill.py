#imports
from machine import Pin
import time

#variables
seconds = 0
n_cycle = 0
n_blades = 3

#functions
"""
def clock(seconds):
    time.sleep(1)
    seconds += 1
    return seconds"""

def changed(x, n):
    n = n%2
    values = []
    values[n] = x
    average = (values[0] + values[1])/2
    if average != values[n]:
        return True
    else:
        return False

def rpm(x):
    blades_seen = 0
    if changed(infared_sensor.value(), n_cycle):
        blades_seen += 1


#pins
output = Pin(14, Pin.OUT)
infared_sensor = Pin(15, Pin.IN)

#main
while True:
    n_cycle =+ 1

    print(infared_sensor.value())
    if infared_sensor.value() == 0:
        output.value(1)
    else:
        output.value(0)
