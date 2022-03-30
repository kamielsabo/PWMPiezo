#!/usr/bin/env python3.2.3
# Date And Time Script

from time import sleep
from datetime import datetime, timedelta

import pwmpump
import pwmmotor
import requests
import sensors

if __name__ == "__main__":
    # Define sensor channel
    temp_channel = 0
    # Query buffer start parameters
    today_plus_delta = datetime.now()
    now = datetime.now()
    seconds_to_new_query = 0
    stop_alarm = False
    datetime_alarm = requests.get('https://studev.groept.be/api/a21ib2b02/readnext').json()
    volume = int(requests.get('https://studev.groept.be/api/a21ib2b02/get_volume').json()[0]['volume'])
    if datetime_alarm:
        a = str(datetime_alarm[0]['alarm_datetime'])
        alarm_datetime = datetime(int(a[:4]), int(a[5:7]), int(a[8:10]), int(a[11:13]), int(a[14:16]))
        alarm = alarm_datetime
    else:
        alarm = datetime.now() + timedelta(days=365)

    while True:
        # X - Always check for the next alarm
        # count down and database push/pull code will probably come here
        # get the date and time for now

        seconds_to_new_query = (today_plus_delta - datetime.now()).total_seconds()

        if seconds_to_new_query < 0:
            stop_alarm = False
            print("Sending query to database...")
            volume = int(requests.get('https://studev.groept.be/api/a21ib2b02/get_volume').json()[0]['volume'])
            print(volume)
            datetime_alarm = requests.get('https://studev.groept.be/api/a21ib2b02/readnext').json()

            # Duplicate code that will be removed
            if len(datetime_alarm) != 0:
                a = str(datetime_alarm[0]['alarm_datetime'])
                # print(a)
                # print(a[:4], a[5:7], a[8:10], a[11:13], a[14:])
                alarm_datetime = datetime(int(a[:4]), int(a[5:7]), int(a[8:10]), int(a[11:13]), int(a[14:16]))
                alarm = alarm_datetime

            now = datetime.now()
            # get now plus 10 seconds
            today_plus_delta = now + timedelta(seconds=30)

        time_left = alarm - datetime.now()

        if time_left < timedelta(seconds=0) and not stop_alarm and len(datetime_alarm) != 0:
            print("Starting to make coffee...")
            sleep(0.2)
            # turn pump ON
            pwmpump.pump_water(volume)
            stop_alarm = True
            # then turn the coffee machine ON
            pwmmotor.switch_coffee_machine()

        # X - Always check ldr
        # Code for the ntc sensor

        # Read the temperature sensor data
        temp_level = sensors.ReadChannel(temp_channel)
        temp_volts = sensors.ConvertVolts(temp_level, 2)
        temp = sensors.ConvertTemp(temp_volts, 2)

        print(temp)
        print(temp_volts)

        # # Define LED states
        # if light_volts > 2.0:
        #     GPIO.output(36, 1)
        # else:
        #     GPIO.output(36, 0)