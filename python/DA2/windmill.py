#imports
from machine import Pin
import time

#variables
i_know_what_im_doing = False
cycle = 0
change_count = 0

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

def change_counter(a):
    if changed(infared_sensor.value(), cycle):
        global change_count
        change_count += 1
        return change_count
    else:
        global change_count
        return change_count

def rotational_calc(times):
    differences = [times[4] - times[2],
                   times[2] - times[0],
                   times[0] - times[4]]
    differences[0] = 60 / (differences[0] * 3)
    differences[1] = 60 / (differences[1] * 3)
    differences[2] = 60 / (differences[2] * 3)
    average_segment_time = sum(differences)/3
    return average_segment_time

def rpm(changes):
    x = changes % 6

    times = []

#pins
output = Pin(14, Pin.OUT)
infared_sensor = Pin(15, Pin.IN)

#main
while True:
    rpm(cycle)
    cycle =+ 1 #counts how many times program has been run

    print(infared_sensor.value())
    if infared_sensor.value() == 0:
        output.value(1)
    else:
        output.value(0)
