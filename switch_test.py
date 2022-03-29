import gpiozero
from datetime import datetime, timedelta

# setup servo
servo = gpiozero.Servo(12)
servo.max()

# setup time interval that button is pressed
timeMid = 0.5
stopTime = datetime.now() + timedelta(seconds=timeMid)
pressing = True

# press button
servo.mid()
while pressing:
    if stopTime - datetime.now() < timedelta(seconds = 0):
        pressing = False

#setup time interval to release button
timeMax = 0.5
stopTime = datetime.now() + timedelta(secpnds=timeMax)

# release button
releasing = True
servo.max()
while releasing:
    if stopTime - datetime.now() < timedelta(seconds = 0):
        releasing = False
