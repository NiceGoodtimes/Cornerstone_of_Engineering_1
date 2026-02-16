"""Euler's method
x = 1.0
y = 1.0
dx = 0.1

while x <= 2.5:
    f = x + 3 * y/x
    y = y + f*dx
    x = x +dx
    print(f"x = {x:.3} y = {y:.3}")"""
"""
bala1 = 1.0
bala2 = 2.0
bala3 = 100
bala4 = (bala2-bala1)/bala3
bala5 = bala1**2
bala6 = bala2**2

bala = 0.5*(bala5+bala6)*bala4
for bala0 in range(1,bala3,1):
    bala7 = bala1+bala0*bala4
    bala8 = bala7**2
    bala = bala + bala8*bala4
print(f"Bala's Answer = {bala:.4}")
"""
#def re_lister(value, list_length, n, list_to_add_to):
#    n % list_length
#    list_to_add_to[n] = value
#    return list_to_add_to

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
