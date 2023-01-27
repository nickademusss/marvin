import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay

# this sets it so goes by name (e.g. GPIO 3)
GPIO.setmode(GPIO.BCM)


# GPIO.setup(ledpin,GPIO.OUT)
# pwm = GPIO.PWM(ledpin,1000)
# adjusting the voltage supplied to the motor
# pwm.ChangeDutyCycle(duty)

# motor 1 = left
# motor 2 = right

DIR_FORWARD = 0
DIR_BACKWARD = 1

pwm_freq = 10000

motor_1_dir_pin = 5
motor_2_dir_pin = 6

GPIO.setup(motor_1_dir_pin, GPIO.OUT) 
GPIO.setup(motor_2_dir_pin, GPIO.OUT)

motor_1_pwm_pin = 12
motor_2_pwm_pin = 13

GPIO.setup(motor_1_pwm_pin, GPIO.OUT)
GPIO.setup(motor_2_pwm_pin, GPIO.OUT)

pwm_motor_1 = GPIO.PWM(motor_1_pwm_pin, pwm_freq)
pwm_motor_2 = GPIO.PWM(motor_2_pwm_pin, pwm_freq)

# forward by default
def start_right_motor(duty_cycle, direction=0):
    global motor_2_dir_pin, pwm_motor_2
    # direction swapped on this motor since it is on the opposite side
    if(direction == 0):
        direction = 1
    else:
        direction = 0

    GPIO.output(motor_2_dir_pin, direction)
    pwm_motor_2.start(duty_cycle)

def stop_right_motor():
    global pwm_motor_2
    pwm_motor_2.stop()

# forward by default
def start_left_motor(duty_cycle, direction=0):
    global motor_1_dir_pin, pwn_motor_1
    GPIO.output(motor_1_dir_pin, direction)
    pwm_motor_1.start(duty_cycle)

def stop_left_motor():
    global pwm_motor_1
    pwm_motor_1.stop()


#start_left_motor(25, direction = DIR_BACKWARD)
#start_left_motor(25, direction = DIR_FORWARD)
#sleep(5)
#stop_left_motor()

#start_right_motor(25, direction = DIR_BACKWARD)
#start_right_motor(25, direction = DIR_FORWARD)
#sleep(5)
#stop_right_motor()

center_bumper_pin = 27;
left_bumper_pin = 26;
right_bumper_pin = 23;

GPIO.setup(center_bumper_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(left_bumper_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(right_bumper_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

center_bumper_pin = 27;
def is_collision():

    if(GPIO.input(center_bumper_pin) == 1):
        return True
    if(GPIO.input(left_bumper_pin) == 1):
        return True
    if(GPIO.input(right_bumper_pin) == 1):
        return True

    return False

duty_cycle = 25 
while(True):

    try:
        start_left_motor(duty_cycle, direction = DIR_FORWARD)
        start_right_motor(duty_cycle, direction = DIR_FORWARD)

        while(not is_collision()):
            pass

        start_left_motor(duty_cycle, direction = DIR_BACKWARD)
        start_right_motor(duty_cycle, direction = DIR_BACKWARD)
        sleep(1)

        start_left_motor(duty_cycle, direction = DIR_BACKWARD)
        start_right_motor(duty_cycle, direction = DIR_FORWARD)
        sleep(1)
    except KeyboardInterrupt:
        break

stop_left_motor()
stop_right_motor()

GPIO.cleanup()

