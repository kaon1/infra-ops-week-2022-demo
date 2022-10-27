import requests

city_name = 'paris'

get_geoid = requests.get('https://api.teleport.org/api/cities/?search='+city_name).json()

#get_geoid_result = get_geoid.json()

city_info_url = get_geoid['_embedded']['city:search-results'][0]['_links']['city:item']['href']

get_city_info = requests.get(city_info_url).json()

country = get_city_info['_links']['city:country']['name']
timezone = get_city_info['_links']['city:timezone']['name']
lat = get_city_info['location']['latlon']['latitude']
long = get_city_info['location']['latlon']['longitude']

print(country)
print(timezone)
print(lat)
print(long)