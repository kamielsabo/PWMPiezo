import gpiozero


def drive_pump():
    out = gpiozero.PWMOutputDevice(18)

    while True:
        out.frequency = 2000
        out.value = 0.3
