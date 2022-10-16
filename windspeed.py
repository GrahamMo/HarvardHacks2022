import requests, json, os
import meteomatics.api as api
import math

import LoginCredentials

class windCalculator():
    def init(self):
        pass
    def get_wind_data(self,lat,lon):
        """Calls api to get average windspeed given long and lat"""
        api_key = os.getenv('api_key')
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + f"&lat={lat}&lon={lon}"
        response = requests.get(complete_url)
        x = response.json()
        #print(x['wind']['speed'])

        return (x['wind']['speed'])

    def get_wind_power(self,radius,velocity):
        '''Calculates wind power from radius of turbine and speed of wind.'''
        rho = 1.225 #average wind density is 1.225 kg/m^3
        area = math.pi * (radius ** 2)
        power = 0.5 * rho * area * (velocity ** 3)
        power = round(power,2)
        return power
    
    def get_20year_savings(self, pow_out):

        upfront_cost = 2000 # approx. purchasing cost of backyard wind turbine

        avg_cost_per_kWh = 0.15 # average cost per kWh in the USA

        # pow_out is in W or Joule/s
        # so convert it to KiloJoule/hour or kWh
        # multiply by average cost per kWh in the usa, and the amount of hours in 20 years
        twentyyear_rev = pow_out * 1/1000 * 60 * avg_cost_per_kWh * 8760 * 20

        total_savings = twentyyear_rev - upfront_cost 

        return [upfront_cost,round(twentyyear_rev,2),round(total_savings,2)]

