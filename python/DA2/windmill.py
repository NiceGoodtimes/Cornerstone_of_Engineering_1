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
microseconds_per_minute = 60000000
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

def timer():
    global times
    assigner = change_count % 3
    if change_count%2 == 0:
        times[assigner] = time.ticks_us()

def rpm():
    global times
    differences = [time.ticks_diff(times[1], times[0]),
                   time.ticks_diff(times[2], times[1]),
                   time.ticks_diff(times[0], times[2])]

    segment_revolution_time = [x*3 for x in differences]

    average_segment_time = sum(differences)/3
    return average_segment_time

#main
while True: #If you have another while true statement, put the following code there instead
    change_counter()
    if times[2] != 0:
        rpm()
    current_rpm = None
    cycle += 1 #counts how many times program has been run
    #check for corruption
