#imports
from machine import Pin
import time

#variables
i_know_what_im_doing = False

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

def rpm(blades):
    changes = 0
    time_of_change = []
    if changed(infared_sensor.value(), n_cycle):
        time_of_change[changes] = time.time()
        changes += 1

#pins
output = Pin(14, Pin.OUT)
infared_sensor = Pin(15, Pin.IN)

#main
while True:
    n_cycle =+ 1 #counts how many times program has been run

    print(infared_sensor.value())
    if infared_sensor.value() == 0:
        output.value(1)
    else:
        output.value(0)
