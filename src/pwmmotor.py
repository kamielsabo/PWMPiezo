from gpiozero import Servo
from time import sleep


def drive_motor():
    servo = Servo(12)

    while True:
        servo.min()
        sleep(5)
        servo.mid()
        sleep(5)
        servo.max()
        sleep(5)
