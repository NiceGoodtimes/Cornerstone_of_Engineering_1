"""NOTES:
-replaced time with milliseconds for greater accuracy
"""

#imports
from machine import Pin
import time

#variables & pins
infrared_sensor = Pin(15, Pin.IN)

change_count = 0
sections = 3
microseconds_per_minute = 60000000
lv_infrared = infrared_sensor.value()
times = [0, 0, 0]

#functions
def changed():
    global lv_infrared
    current_value = infrared_sensor.value()
    if lv_infrared != current_value:
        lv_infrared = current_value
        return True
    else:
        return False

def change_counter():
    global change_count
    if changed():
        change_count += 1
        change_count = change_count % 6
        return change_count
    else:
        return change_count

def timer():
    global times
    assigner = change_count % 3
    if change_count%2 == 0:
        times[assigner] = time.ticks_us()

def rpm():
    global times
    timer()
    if times[2] != 0:
        differences = [time.ticks_diff(times[1], times[0]),
                       time.ticks_diff(times[2], times[1]),
                       time.ticks_diff(times[0], times[2])]

        segment_rpm = [microseconds_per_minute/(x*3) for x in differences]

        average_segment_time = sum(segment_rpm)/3
        return average_segment_time
    else: return 0.0

#main
while True: #If you have another while true statement, put the following code there instead
    change_counter()
    if times[2] == 0:
        continue
    current_rpm = rpm()
    #check for corruption
