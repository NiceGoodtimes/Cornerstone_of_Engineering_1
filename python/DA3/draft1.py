#imports
import machine
from machine import Pin, PWM
import time

#global variables
photo_left_raw = machine.ADC(27)
photo_right_raw = machine.ADC(26)
servo_out = PWM(Pin(0))
servo_out.freq(50)

#functions
def scaling(photo_pin) -> int:
    raw = photo_pin.read_16()
    return raw // 5000

def balance(left: int, right:int):
    diff = right - left
    if diff < 0:
        return abs(diff), "L"
    else:
        return abs(diff), "R"

#main
while True:
    pass
