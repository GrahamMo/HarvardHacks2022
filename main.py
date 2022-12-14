#import solar.py
import windspeed
import solar
from flask import Flask, request
from geopy.geocoders import Nominatim


app = Flask(__name__)

#-------------------------------
#END POINT

@app.route("/")
def default():
    return "Online", 

@app.route("/result", methods = ["GET"])
def get_results():
    address = request.args.get('address')

    geolocator = Nominatim(user_agent="Solar Calc")
    location = geolocator.geocode(address)

    solar_calc = solar.solarCalculator()
    solar_data = solar_calc.get_data(location.latitude, location.longitude)

    wind_calc = windspeed.windCalculator()
    wind_speed = wind_calc.get_wind_data(location.latitude, location.longitude)
    exp_wind_pout = wind_calc.get_wind_power(0.5, wind_speed)

    upfront_cost = wind_calc.get_20year_savings(exp_wind_pout)[0]
    twentyyear_rev = wind_calc.get_20year_savings(exp_wind_pout)[1]
    total_savings = wind_calc.get_20year_savings(exp_wind_pout)[2]

    response = [("Upfront cost: $" + str(upfront_cost)),("20 Year Benefits: $" \
        + str(twentyyear_rev)),("By installing a Backyard Wind Turbine you will save $"\
             + str(total_savings) + "over the course of 20 years.")]

    return response





app.run("0.0.0.0", 5000) #run the app. first parameter indicates bind from anywhere (take all requests) and the 2nd is prot