import gpiozero
import time
from datetime import datetime, timedelta


out = gpiozero.PWMOutputDevice(13)
out.frequency = 200
out.value = 0.5
newNow = datetime.now() + timedelta(seconds=5)
booleanTime = True

while booleanTime:
    if newNow - datetime.now() < timedelta(seconds=0):
        booleanTime = False

out.off()

