# API Request to grab weather forecast of 3 different cities and print the precipitation type
import requests

list_of_coordinates = [{'city_name': 'Dublin', 'long': '53.350',  'lat': '-6.256'},{'city_name': 'Paris', 'long': '48.856', 'lat': '2.352'},{'city_name': 'Seattle', 'long': '47.607', 'lat': '-122.334'}]

for entry in list_of_coordinates:
    ## example api call to get weather forecast https://www.7timer.info/bin/astro.php?lon=53.350&lat=-6.256&unit=metric&output=json
    weather_forecast_api_call = requests.get("https://www.7timer.info/bin/astro.php?lon="+entry['long']+"&lat="+entry['lat']+"&unit=metric&output=json")
    weather_forecast_result = weather_forecast_api_call.json()
    print("The precipitation forecast in "+entry['city_name']+" is: "+weather_forecast_result['dataseries'][0]['prec_type'])
