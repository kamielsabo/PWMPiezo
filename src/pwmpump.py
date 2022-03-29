import gpiozero
import time
from datetime import datetime, timedelta

def pump_water(volumeCl):
    timeToRun = (10*volumeCl) / 29.52
    out = gpiozero.PWMOutputDevice(13)
    out.frequency = 200
    out.value = 0.2
    newNow = datetime.now() + timedelta(seconds=timeToRun)
    booleanTime = True

    while booleanTime:
        if newNow - datetime.now() < timedelta(seconds=0):
            booleanTime = False

    out.off()



