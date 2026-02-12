#imports
from machine import Pin
import time

#variables
i_know_what_im_doing = False
num_blades = 3
changes = 0

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
    for interval in differences:
        interval = (interval*3)/60
    average_segment_time = sum(differences)/3
    return average_segment_time



def rpm(blades):
    if n_cycle == 0:
        global changes
        changes = 0
    time_of_change = []
    if changed(infared_sensor.value(), n_cycle):
        changes = changes % 6
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
