import requests, json, os
import meteomatics.api as api

import LoginCredentials

def get_wind_data():
    api_key = os.getenv('api_key')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    lat = 35
    lon = 139
    complete_url = base_url + "appid=" + api_key + f"&lat={lat}&lon={lon}"
    response = requests.get(complete_url)
    x = response.json()
    print(x['wind']['speed'])

    return True

get_wind_data()
