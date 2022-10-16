import requests, json, os
import meteomatics.api as api
import math
from flask import Flask, request
from geopy.geocoders import Nominatim
import windspeed
import solar

def display(response):

    print("\n"+response[0]+"\n")
    print(response[1]+"\n")
    print(response[2]+"\n")

    return True

def main():
    address = input("Enter Address: ")

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)

    #solar_calc = solar.solarCalculator()
    #solar_data = solar_calc.get_data(location.latitude, location.longitude)

    wind_calc = windspeed.windCalculator()
    wind_speed = wind_calc.get_wind_data(location.latitude, location.longitude)
    exp_wind_pout = wind_calc.get_wind_power(0.5, wind_speed)

    upfront_cost = wind_calc.get_20year_savings(exp_wind_pout)[0]
    twentyyear_rev = wind_calc.get_20year_savings(exp_wind_pout)[1]
    total_savings = wind_calc.get_20year_savings(exp_wind_pout)[2]

    response = [("Upfront cost: $" + str(upfront_cost)),("20 Year Benefits: $" \
        + str(twentyyear_rev)),("By installing a Backyard Wind Turbine you will save $"\
             + str(total_savings) + " over the course of 20 years.")]

    display(response)
    return True

main()