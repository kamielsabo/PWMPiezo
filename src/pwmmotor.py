from gpiozero import Servo
from time import sleep

servo = Servo(12)
servo.min_pulse_width = 1.5
servo.max_pulse_width = 1.9

while True:
    servo.min()
    sleep(5)
    servo.mid()
    sleep(5)
    servo.max()
    sleep(5)
