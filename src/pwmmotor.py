from gpiozero import Servo
from time import sleep

servo = Servo(12)

while True:
    servo.max()
    sleep(5)
    servo.min()
    sleep(5)
