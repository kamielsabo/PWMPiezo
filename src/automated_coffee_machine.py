#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep
import gpiozero
import time
from datetime import datetime, timedelta

import databank_retriever
import pump
import switch
import requests
import temperature_regulator


if __name__ == "__main__":
    #Instantiate objects
    temp_regulator = temperature_regulator.TemperatureRegulator()
    data_retriever = databank_retriever.DatabankRetriever()
    coffee_switch = switch.Switch()
    water_pump = pump.Pump()

    # variables
    temperature_setting_next_pot = "MEDIUM"

    # Query buffer start parameters
    today_plus_delta = datetime.now()   # initially set to now such that first run is executed, afterwards is autoupdated
    now = datetime.now()
    seconds_to_new_query = 0
    coffee_is_being_made = False
    time_coffee_was_set = datetime.now() - timedelta(minutes=15)   # Sets to 15 minutes earlier for the first run, auto updates after
    datetime_alarm = data_retriever.get_alarm_time()
    volume = data_retriever.get_volume()
    if not datetime_alarm:
        a = str(datetime_alarm[0]['alarm_datetime'])
        alarm = datetime(int(a[:4]), int(a[5:7]), int(a[8:10]), int(a[11:13]), int(a[14:16]))
    else:
        alarm = datetime.now() + timedelta(days=365)

    # loop
    while True:
        seconds_to_new_query = (today_plus_delta - datetime.now()).total_seconds()

        if seconds_to_new_query < 0:
            print("\n")
            if coffee_is_being_made:
                print("Coffee is being made")
                print("Coffee will be held at " + str(temp_regulator.get_temperature_center()) + "°C")
                temp_regulator.regulate()
            else:
                print("Sending query to database...")

            volume = data_retriever.get_volume()
            datetime_alarm = data_retriever.get_alarm_time()
            if datetime_alarm:
                a = data_retriever.get_alarm_time()
                alarm = datetime(int(a[:4]), int(a[5:7]), int(a[8:10]), int(a[11:13]), int(a[14:16]))

            # get now plus 10 seconds
            today_plus_delta = datetime.now() + timedelta(seconds=30)

            temperature_setting_next_pot = data_retriever.get_temperature()

        time_left = alarm - datetime.now()
        if time_left < timedelta(seconds=0) and not coffee_is_being_made:
            print("Starting to make coffee...")
            time_coffee_was_set = datetime.now()
            temp_regulator.set_temperature_regulator(str(temperature_setting_next_pot))
            print("Coffee will be held " + str(temperature_setting_next_pot) + " at " + str(temp_regulator.get_temperature_center()) + "°C")
            coffee_is_being_made = True
            # turn pump ON
            water_pump.pump_water(volume)
            # then turn the coffee machine ON
            coffee_switch.switch_coffee_machine()

        if datetime.now() - time_coffee_was_set > timedelta(minutes=15):
            coffee_is_being_made = False

