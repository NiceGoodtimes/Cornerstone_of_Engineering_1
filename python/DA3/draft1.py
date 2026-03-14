#imports
import machine
from machine import Pin, PWM
import time

#global variables
photo_left_raw = machine.ADC(27) #photoresistors quantify brightness
photo_right_raw = machine.ADC(26)
servo_out = PWM(Pin(0))
servo_out.freq(50)

#functions
"""Photoresistor functions"""
def downstep(photo_pin): #scales down photoresistor output
    raw = photo_pin.read_16()
    return raw // 5000

def balance(left: int, right:int): #determines which side receives more light
    diff = right - left
    if diff < 0:
        return [abs(diff), "L"]
    elif diff > 0:
        return [abs(diff), "R"]
    else:
        return [0, "C"]

"""servo functions"""
def set_servo(mode: int): #sets the mode of the servo
    servo_out.duty_u16(mode)

def spinner(x: list): #determines how to spin the servo
    forward = 6553
    stop = 4915
    reverse = 3277

    if x[2] == "R":
        set_servo(forward)
        time.sleep_ms(10)
        set_servo(stop)
    elif x[2] == "L":
        set_servo(reverse)
        time.sleep_ms(10)
        set_servo(stop)
    else:
        pass
    """
    Idea: divide full circle of servo range into 14 sections (0:13)
    -> each section is similarly subdivided
    -> magnitude of the difference determines how many subsections are added
        or taken away based off of L / R dominance
    -> resets to be relative to current section
    """

#main
while True:
    left_real = downstep(photo_left_raw)
    right_real = downstep(photo_right_raw)
    pass
