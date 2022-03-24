import gpiozero
import time
from datetime import datetime, timedelta


out = gpiozero.PWMOutputDevice(13)
out.frequency = 200
out.value = 0.2
newNow = datetime.now() + timedelta(seconds=4)
booleanTime = True

while booleanTime:
    if newNow - datetime.now() < timedelta(seconds=0):
        booleanTime = False

out.off()

