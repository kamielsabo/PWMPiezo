import gpiozero
import time
from datetime import datetime, timedelta


out = gpiozero.PWMOutputDevice(13)
out.frequency = 100
out.value = 0.3
newNow = datetime.now() + timedelta(seconds=5)
booleanTime = True

while booleanTime:
    out.on
    if newNow - datetime.now() < timedelta(seconds=0):
        booleanTime = False

while True:
    out.off

