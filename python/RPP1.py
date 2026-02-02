"""DISCLAIMER: sections of this code were sampled from Northeastern's FYELIC examples.
I simply integrated two examples into one using my own preference of writing (bad through it may be)"""
from machine import Pin
import time

#photoresistor
photoresistor_pin = 27
photoresistor = machine.ADC(photoresistor_pin)
#led pins
led_pin = 15
led = Pin(led_pin, Pin.OUT)


#functions
def lighting_control(threshold):
    if threshold <= 3000:
        led.on()
    else:
        led.off()

#main
while True:
    resistor_result = photoresistor.read_u16()-60000
    print(resistor_result)
    lighting_control(resistor_result)
    time.sleep(1)  # 1-second delay
