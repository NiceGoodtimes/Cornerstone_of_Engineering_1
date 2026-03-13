#imports
import machine
from machine import Pin, PWM
import time

#global variables
photo_left_raw = machine.ADC(27)
photo_right_raw = machine.ADC(26)
servo_out = PWM(Pin(0))
servo_out.freq(50)

current_section = 0

#functions
def downstep(photo_pin) -> int:
    raw = photo_pin.read_16()
    return raw // 5000

def balance(left: int, right:int):
    diff = right - left
    if diff < 0:
        return abs(diff), "L"
    else:
        return abs(diff), "R"

def spinner():
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
    pass
