import requests
import spidev
from numpy import log as ln


temperature_to_be_held = "COLD"     # set to cold temperature by default


def set_temperature_regulator(temp_to_be_held):
    temperature_to_be_held = temp_to_be_held


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
