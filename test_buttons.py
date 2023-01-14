# this is our script for testing GPIO buttons on our raspberry pi controller
import RPi.GPIO as GPIO
import time

# can be board or GPIO
GPIO.setmode(GPIO.BCM)

button_1_pressed = False

button_events = []
button_states = {}

# GPIO Setup
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button_states["RED_BUTTON"] = [False, 24]

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button_states["BLUE_BUTTON"] = [False, 25]

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button_states["LEFT_BUMP"] = [False, 26]

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button_states["CENTER_BUMP"] = [False, 27]

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button_states["RIGHT_BUMP"] = [False, 23]



button_map = {}
for state in button_states:
    pin_num = button_states[state][1]
    button_map[pin_num] = state

# check for button input with debouncing
def check_button_for_input(btn_number):
    global button_events

    if(GPIO.input(btn_number) == 1 and not button_states[button_map[btn_number]][0]):
        time.sleep(.05)
        if(GPIO.input(btn_number) == 1):
            button_states[button_map[btn_number]][0] = True
            button_events.append(button_map[btn_number])
            return True

    elif(GPIO.input(btn_number) == 0):
            button_states[button_map[btn_number]][0] = False 


def handle_button_events():
    print(button_events)
    button_events.pop()
    pass

while True:
    for button in button_map:
        check_button_for_input(button)

    if(len(button_events) > 0):
        handle_button_events()
