import requests
import datetime


upcomming_settings = requests.get('https://studev.groept.be/api/a21ib2b02/get_coffee_next').json()


def get_temperature():
    return str(upcomming_settings[0]["temp"])


def get_volume():
    return int(upcomming_settings[0]['volume'])


def get_alarm_time():
    return upcomming_settings[0]["alarm_datetime"]

print(upcomming_settings)
print(get_temperature())
print(get_volume())
print(get_alarm_time())