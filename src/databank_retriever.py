import requests
import datetime

class DatabankRetriever:
    def __init__(self):
        self.upcomming_settings = requests.get('https://studev.groept.be/api/a21ib2b02/get_coffee_next').json()

    def get_temperature(self):
        return str(self.upcomming_settings[0]["temp"])

    def get_volume(self):
        return int(self.upcomming_settings[0]['volume'])

    def get_alarm_time(self):
        return self.upcomming_settings[0]["alarm_datetime"]
