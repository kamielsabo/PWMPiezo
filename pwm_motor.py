import gpiozero

out = gpiozero.PWMOutputDevice(12)

while True:
    out.frequency = 900
    out.value = 0.5
