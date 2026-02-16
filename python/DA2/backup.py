"""
Still need: put in while true
Potentially: change time to be ms for accuracy
"""

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

def change_counter():
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

def rpm(changes, run_cycle):
    x = changes % 6
    time_list = []

    if changed(changes, run_cycle):
        time_list[x] = time.time()
        return time_list
    else:
        return time_list


#pins
output = Pin(14, Pin.OUT)
infared_sensor = Pin(15, Pin.IN)

#main
while True: #If you have another while true statement, put the following code there instead
    current_rpm = rotational_calc(rpm(change_count, cycle))
    cycle =+ 1 #counts how many times program has been run

#-----------------------------Backup 2-----------------------------------------------------
"""NOTES:
- replace math for milliseconds
"""

#imports
from machine import Pin
import time

#variables & pins
infrared_sensor = Pin(15, Pin.IN)

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

    segment_rpm = [microseconds_per_minute/(x*3) for x in differences]

    average_segment_time = sum(segment_rpm)/3
    return average_segment_time

#main
while True: #If you have another while true statement, put the following code there instead
    change_counter()
    if times[2] == 0:
        continue
    current_rpm = rpm()
    #check for corruption

#----------------------Backup 3----------------------------------
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

    segment_rpm = [microseconds_per_minute/(x*3) for x in differences]

    average_segment_time = sum(segment_rpm)/3
    return average_segment_time

#main
while True: #If you have another while true statement, put the following code there instead
    change_counter()
    if times[2] == 0:
        continue
    current_rpm = rpm()
    #check for corruption

