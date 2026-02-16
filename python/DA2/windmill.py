"""NOTES:
- replace math for milliseconds
"""

#imports
from machine import Pin
import time

#variables & pins
infrared_sensor = Pin(15, Pin.IN)

cycle = 0
change_count = 0
sections = 3
last_value_infrared = infrared_sensor.value()
times = [0, 0, 0]

#functions
def changed():
    global last_value_infrared
    current_value = infrared_sensor.value()
    if last_value_infrared != current_value:
        last_value_infrared = current_value
        return True
    else:
        return False

def change_counter():
    global change_count
    if changed():
        change_count += 1
        return change_count % 6
    else:
        return change_count

def revolution_calc():
    global times
    differences = []


    differences[0] = 60 / (differences[0] * sections)
    differences[1] = 60 / (differences[1] * sections)
    differences[2] = 60 / (differences[2] * sections)
    average_segment_time = sum(differences)/3
    return average_segment_time

def rpm():
    pass

#main
while True: #If you have another while true statement, put the following code there instead
    current_rpm = None
    cycle += 1 #counts how many times program has been run
    #check for corruption
