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
DIR_BACKWARDS = 1

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

GPIO.output(motor_1_dir_pin, DIR_FORWARD)
GPIO.output(motor_2_dir_pin, DIR_BACKWARDS)

# 25% duty cycle
pwm_motor_1.start(25)
pwm_motor_2.start(25)
sleep(2.5)
pwm_motor_2.stop()
pwm_motor_1.stop()


GPIO.cleanup()
