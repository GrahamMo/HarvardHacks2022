import requests, json, os
import meteomatics.api as api
import math

import LoginCredentials

class windCalculator():
    def init(self):
        pass
    def get_wind_data(self):
        api_key = os.getenv('api_key')
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        lat = 42.380960
        lon = -71.125240
        complete_url = base_url + "appid=" + api_key + f"&lat={lat}&lon={lon}"
        response = requests.get(complete_url)
        x = response.json()
        #print(x['wind']['speed'])

        return (x['wind']['speed'])

    def get_wind_power(self,radius,velocity):

        rho = 1.225 #average wind density is 1.225 kg/m^3

        area = math.pi * (radius ** 2)

        power = 0.5 * rho * area * (velocity ** 3)

        power = round(power,2)

        return power

