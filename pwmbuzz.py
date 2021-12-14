import gpiozero

out = gpiozero.PWMOutputDevice(18)


while True:
    out.frequency = 5000
    out.value = 0.7
