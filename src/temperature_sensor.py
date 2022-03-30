import sensors

data = sensors.ReadChannel(0)
volts = sensors.ConvertVolts(data, 3)
print("Volts: " + str(volts))
temp = sensors.ConvertTemp(volts, 2)
print(temp)
