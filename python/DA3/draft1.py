#imports
import machine
from machine import Pin, PWM
import time

#global variables
photo_left_pin = machine.ADC(27) #photoresistors quantify brightness
photo_right_pin = machine.ADC(26)
servo_out = PWM(Pin(0))
servo_out.freq(50)

#functions
"""Photoresistor functions"""
def downstep(photo_pin): #scales down photoresistor output
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
    servo_out.duty_u16(mode)

def spinner(x): #determines how to spin the servo
    forward = 6553
    stop = 4915
    reverse = 3277

    if x == "R":
        set_servo(forward)
        time.sleep_ms(10)
        set_servo(stop)
    elif x == "L":
        set_servo(reverse)
        time.sleep_ms(10)
        set_servo(stop)
    else:
        pass

#main
while True:
    left_raw = photo_left_pin.read_u16()
    right_raw = photo_right_pin.read_u16()

    left_real = downstep(left_raw)
    right_real = downstep(right_raw)

    spinner(balance(left_real, right_real))