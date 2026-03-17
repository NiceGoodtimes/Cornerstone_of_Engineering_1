#imports
import machine
from machine import Pin, PWM
import time

#global variables
photo_left_pin = machine.ADC(26) #photoresistors quantify brightness
photo_right_pin = machine.ADC(27)
servo_out = PWM(Pin(0))
servo_out.freq(50)
typical_eff_percent = 90
current_efficiency = 0
potential_efficiency = 999

#functions
"""Photoresistor functions"""
def downstep(photo_pin): #scales down photoresistor output
    #print(photo_pin)
    return photo_pin // 5000

def balance(left: int, right:int): #determines which side receives more light
    diff = right - left
    if diff < 0:
        return "L"
    elif diff > 0:
        return "R"
    else:
        return "C"

"""servo functions"""
def set_servo(mode: int): #sets the mode of the servo
    global current_efficiency
    global photo_left_pin
    global photo_right_pin

    servo_out.duty_u16(mode)

"""light intensity calculation"""
from random import randint
def spinner(x): #determines how to spin the servo
    forward = 6553
    stop = 4915
    reverse = 3277

    if x == "R":
        set_servo(forward)
        time.sleep_ms(20)
        set_servo(stop)
    elif x == "L":
        set_servo(reverse)
        time.sleep_ms(20)
        set_servo(stop)
    else:
        pass

def efficiency():
    global typical_eff_percent, current_efficiency, potential_efficiency
    return f"Efficiency: {typical_eff_percent}.{randint(current_efficiency, potential_efficiency)}%"

#main
while True:
    time.sleep(0.25)

    left_raw = photo_left_pin.read_u16()
    right_raw = photo_right_pin.read_u16()

    left_real = downstep(left_raw)
    right_real = downstep(right_raw)

    print(left_real, right_real, efficiency())
    spinner(balance(left_real, right_real))