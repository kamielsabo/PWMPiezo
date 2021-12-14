import gpiozero

out = gpiozero.PWMOutputDevice(18)
#out.frequency(10000.0)
out.value(0.7)
