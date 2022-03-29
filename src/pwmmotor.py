import gpiozero
import time

def switch_coffee_machine():
    servo = gpiozero.Servo(12)
    servo.max()
    time.sleep(5)
    servo.mid()
    time.sleep(0.5)
