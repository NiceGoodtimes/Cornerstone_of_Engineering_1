"""imports"""
from machine import Pin, PWM
import time

"""variables"""
#pins
buzzer_pin = 0
button1_pin = 13
button2_pin = 14
button3_pin = 15
button1 = Pin(button1_pin, Pin.IN, Pin.PULL_UP)
button2 = Pin(button2_pin, Pin.IN, Pin.PULL_UP)
button3 = Pin(button3_pin, Pin.IN, Pin.PULL_UP)

#objects
buzzer = PWM(Pin(buzzer_pin))
buzzer.freq(1000)  #initial frequency

notes = { #note frequencies (in Hz)
    # Single button presses
    (False, False, False): 262,  #silence
    (True, False, False): 294,  # Button 1 - C4
    (False, True, False): 330,  # Button 2 - D4
    (False, False, True): 349,  # Button 3 - E4

    # Two button combinations
    (True, True, False): 392,  # Buttons 1+2 - F4
    (True, False, True): 440,  # Buttons 1+3 - G4
    (False, True, True): 494,  # Buttons 2+3 - A4

    # All three buttons
    (True, True, True): 523,  # Buttons 1+2+3 - B4
}


def read_buttons():
    """Read button states and return as tuple"""
    # Note: Buttons are active LOW with pull-up resistors. This is why the 'not' is there.
    btn1_pressed = not button1.value()
    btn2_pressed = not button2.value()
    btn3_pressed = not button3.value()

    return btn1_pressed, btn2_pressed, btn3_pressed


def play_note(tone):
    if tone > 0:
        buzzer.freq(tone)
        buzzer.duty_u16(32768)
    else:
        buzzer.duty_u16(0)


def get_note_name(button_combo):
    note_names = {
        (False, False, False): "C - Low",
        (True, False, False): "D",
        (False, True, False): "E",
        (False, False, True): "F",
        (True, True, False): "G",
        (True, False, True): "A",
        (False, True, True): "B",
        (True, True, True): "C",
    }
    return note_names.get(button_combo, "Unknown")


print("Digital Trumpet Ready!")
print("Press buttons to play notes:")

# Keep track of previous button state to reduce console spam
previous_buttons = (False, False, False)

while True:
    current_buttons = read_buttons()

    if current_buttons != previous_buttons:
        frequency = notes.get(current_buttons, 0)
        play_note(frequency)
        note_name = get_note_name(current_buttons)
        if frequency > 0:
            print(f"Playing: {note_name} ({frequency} Hz)")
        else:
            print("Silence")
        previous_buttons = current_buttons
    time.sleep(0.05)  # Small delay for responsive but not overwhelming updates