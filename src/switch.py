import gpiozero
from datetime import datetime, timedelta

class Switch:
    def __init__(self):
        self.servo = gpiozero.Servo(12)

    def switch_coffee_machine(self):
        # setup servo
        self.servo.max()

        # setup time interval that button is pressed
        timeMid = 0.5
        stopTime = datetime.now() + timedelta(seconds=timeMid)
        pressing = True

        # press button
        self.servo.mid()
        while pressing:
            if stopTime - datetime.now() < timedelta(seconds = 0):
                pressing = False

        #setup time interval to release button
        timeMax = 0.5
        stopTime = datetime.now() + timedelta(seconds=timeMax)

        # release button
        releasing = True
        self.servo.max()
        while releasing:
            if stopTime - datetime.now() < timedelta(seconds = 0):
                releasing = False
