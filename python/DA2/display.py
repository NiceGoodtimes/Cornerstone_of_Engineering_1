import utime
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep
import time

adc0 = machine.ADC(26)  # ADC0 pin is GP26
voltage = 0

# variables & pins
infrared_sensor = Pin(15, Pin.IN)

change_count = 0
sections = 3
microseconds_per_minute = 60000000
last_value_infrared = infrared_sensor.value()
times = [0, 0, 0]


# functions
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
    if change_count % 2 == 0:
        times[assigner] = time.ticks_us()


def rpm():
    global times
    differences = [time.ticks_diff(times[1], times[0]),
                   time.ticks_diff(times[2], times[1]),
                   time.ticks_diff(times[0], times[2])]

    segment_rpm = [microseconds_per_minute / (x * 3) for x in differences]

    average_segment_time = sum(segment_rpm) / 3
    return average_segment_time


for i in range(1, 100):
    # read ADC input on pin ADC0 as 16-bit integer (0 - 65535)
    adc_value = adc0.read_u16()
    # Convert analog reading (0 - 65535) to a voltage (0 - 3.3V)
    adc_voltage = adc_value * (3.3 / 65536)
    # send data to computer over USB
    voltage = voltage + adc_voltage
    # delay half a second
    utime.sleep(0.1)
    print(adc_voltage)
    average = voltage / i

current_rpm_string = f"RPM: {current_rpm:.3} \nVoltage:{average:.2}"

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # Data pin is pin 0, clock pin is pin 1
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # 2 rows on LCD, 16 columns


def slowType(lcd, text, delay=0.1):  # Defines the function to display text
    for i in text:  # Reads text as a list, one letter at a time
        lcd.putstr(i)  # Prints the letter to the LCD
        sleep(delay)  # Defaults to 0.1 second but can be changed when calling function


while True:
    lcd.show_cursor()  # Shows cursor
    lcd.blink_cursor_on()  # Blinks cursor
    slowType(lcd, current_rpm_string, 0.3)  # Function runs
    sleep(1)  # 3 second pause
    lcd.blink_cursor_off()  # Cursor stops blinking
    lcd.hide_cursor()  # Cursor stops
    sleep(1)  # 1 second pause
    lcd.clear()  # Clears screen