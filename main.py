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
    return ""

@app.route("/result", methods = ["GET"])
def get_results():
    address = request.args.get('address')

    geolocator = Nominatim(user_agent="Solar Calc")
    location = geolocator.geocode(address)

    solar_calc = solar.solarCalculator()
    solar_data = solar.get_data(location.latitude, location.longitude)

    wind_calc = windspeed.windCalculator()
    wind_speed = wind_calc.get_wind_data(location.latitude, location.longitude)
    exp_wind_pout = wind_calc.get_wind_power(0.5, wind_speed)


    return ""


app.run("0.0.0.0", 5000) #run the app. first parameter indicates bind from anywhere (take all requests) and the 2nd is prot