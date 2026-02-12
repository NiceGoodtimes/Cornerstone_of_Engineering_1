#imports
from machine import Pin
import time

#variables
i_know_what_im_doing = False
num_blades = 3
cycle = 0

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

def rotational_calc(times):
    differences = [times[4] - times[2],
                   times[2] - times[0],
                   times[0] - times[4]]
    differences[0] = 60 / (differences[0] * 3)
    differences[1] = 60 / (differences[1] * 3)
    differences[2] = 60 / (differences[2] * 3)
    average_segment_time = sum(differences)/3
    return average_segment_time



def rpm(times_run):
    if times_run == 0:
        changes = 0
    time_of_change = []
    if changed(infared_sensor.value(), cycle):
        changes = changes % 6
        time_of_change[changes] = time.time()
        changes += 1


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
