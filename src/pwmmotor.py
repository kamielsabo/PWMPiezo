import gpiozero
import time

servo = gpiozero.Servo(12)

while True:
    servo.max()
    time.sleep(5)
    servo.mid()
    time.sleep(0.5)

