"""NOTES:

"""

#imports
from machine import Pin
import time

#variables & pins
cycle = 0
change_count = 0
sections = 3
infrared_sensor = Pin(15, Pin.IN)

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

def change_counter():
    global change_count
    if changed(infrared_sensor.value(), cycle):
        change_count += 1
        return change_count
    else:
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

def rpm(changes, run_cycle):
    x = changes % 6
    time_list = []

    if changed(changes, run_cycle):
        time_list[x] = time.time()
        return time_list
    else:
        return time_list

#main
while True: #If you have another while true statement, put the following code there instead
    current_rpm = rotational_calc(rpm(change_count, cycle))
    cycle += 1 #counts how many times program has been run
    #check for corruption
