from machine import Pin
import utime

#pins
trigger_pin = 2
echo_pin = 3

# Set up trigger pin as output and echo pin as input
trigger = Pin(trigger_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)


def measure_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signal_off = utime.ticks_us()
    while echo.value() == 1:
        signal_on = utime.ticks_us()

    # Calculate time passed
    time_passed = utime.ticks_diff(signal_on, signal_off)
    distance = (time_passed * 0.0343) / 2
    return distance

def print_distance(distance):
    # First line: Distance reading
    print(f"Distance: {distance:.1f}cm")

#main
while True:
    # Print to console for debugging
    print_distance(measure_distance())

    # Update every 0.2 seconds for smooth operation
    utime.sleep(0.2)