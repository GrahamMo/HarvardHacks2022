#import solar.py
import windspeed

wind_calc = windspeed.windCalculator()
wind_speed = wind_calc.get_wind_data()

exp_wind_pout = wind_calc.get_wind_power(0.5,wind_speed)
#exp_solar_pout = 
print(exp_wind_pout)

#if expected_power_output 