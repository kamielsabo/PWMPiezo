import requests
import spidev
from numpy import log as ln


temperature_center = 70     # set to medium temperature by default
temperature_offset = 3      # the allowable offset the actual temperature can have from the center temperature


def set_temperature_regulator(temperature_to_be_held):
    if(temperature_to_be_held is "COLD"):
        temperature_center = 60

    elif(temperature_to_be_held is"MEDIUM"):
        temperature_center = 70

    elif(temperature_to_be_held is "HOT"):
        temperature_center = 80

    else:
        temperature_center = 70     # set to medium temperature if NULL or something uninterpretable


def read_temperature():
    # Open SPI bus
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1000000

    # Read data from ADC
    adc = spi.xfer2([1, (8) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]

    #convert data to voltage and round to 3 decimals
    volts = (data * 3.3) / float(1023)
    volts = round(volts, 2)

    # Convert voltage to temperature and round to 2 decimals
    R_o = 10000
    voltage_src = 3.3
    R_ref = 5000
    A = 3.35402e-03
    B = 2.51094e-04
    C = 3.51094e-04
    D = 1.10518e-07
    R_t = (R_o * volts) / (voltage_src - volts)
    temp = ((A + B * ln(R_t / R_ref) + C * (ln(R_t / R_ref) ** 2) + D * (ln(R_t / R_ref) ** 3)) ** (-1)) - 273.15
    temp = round(temp, 2)

    return temp


def regulate():
    current_temperature = read_temperature()
    print("Coffee is currently " + str(read_temperature()) + "°C")
    if abs(current_temperature - temperature_center) <  temperature_offset:
        print("Coffee temperature")

    elif current_temperature - temperature_center > temperature_offset:
        print("Coffee is too hot, I will cool it down for you")

    elif (current_temperature - temperature_center) < (-temperature_center):
        print("Coffee is too cold, I will warm it up")


def get_temperature_center():
    return temperature_center
