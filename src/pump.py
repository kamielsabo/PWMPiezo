import gpiozero
from datetime import datetime, timedelta

class Pump:
    def __init__(self):
        self.vol_to_pump = 0
        self.out = gpiozero.PWMOutputDevice(13)
    def pump_water(self, volumeCl):
        self.vol_to_pump = 10*volumeCl
        timeToRun = self.vol_to_pump / 29.52
        self.out.frequency = 200
        self.out.value = 0.2
        newNow = datetime.now() + timedelta(seconds=timeToRun)
        booleanTime = True

        while booleanTime:
            if newNow - datetime.now() < timedelta(seconds=0):
                booleanTime = False

        self.out.off()



