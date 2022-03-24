import gpiozero

out = gpiozero.DigitalOutputDevice(13)
out.on()

while True:


