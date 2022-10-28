### This script aggregates what we learned in the previous modules
### Take user input of any City, use public API endpoints to gather interesting data about the City and its Country

## list of free public API endpoints https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
## public apis: https://api.publicapis.org/entries

from pprint import pprint
import requests
import random
import csv

def get_city_info(city_name):
    # get city info from teleport.org api
    # need to first grab the unique ID of the city by searching the API by city name
    get_geoid = requests.get('https://api.teleport.org/api/cities/?search='+city_name).json()
    city_info_url = get_geoid['_embedded']['city:search-results'][0]['_links']['city:item']['href']
    get_city_info = requests.get(city_info_url).json()

    # set city facts to global dictionary called 'gathered_facts'
    gathered_facts['country'] = get_city_info['_links']['city:country']['name']
    gathered_facts['timezone']  = get_city_info['_links']['city:timezone']['name']
    gathered_facts['lat']  = str(get_city_info['location']['latlon']['latitude'])
    gathered_facts['long']  = str(get_city_info['location']['latlon']['longitude'])


def get_forecast(lat,long):
    # get weather forecaast from lat/long of city using 7timer.info api
    weather_forecast_api_call = requests.get("https://www.7timer.info/bin/astro.php?lon="+lat+"&lat="+long+"&unit=metric&output=json").json()

    gathered_facts['precipitation'] = weather_forecast_api_call['dataseries'][0]['prec_type']

def get_current_covid_cases(country):
    # get current covid cases of the Country using disease.sh api
    covid_case_results = requests.get('https://disease.sh/v3/covid-19/countries/'+country+'?yesterday=true&strict=false').json()
    gathered_facts['current_covid_cases'] = covid_case_results['todayCases']
    # also gather total population of the country
    gathered_facts['population'] = covid_case_results['population']

def get_random_universities(country):
    # get 3 random univeristies from the Country using hipolabs api
    # example api call http://universities.hipolabs.com/search?country=france
    all_universities = requests.get("http://universities.hipolabs.com/search?country="+country).json()
    random_seed = random.sample(range(0,len(all_universities)), 3)
    gathered_facts['universities'] = []
    for entry in random_seed:
        gathered_facts['universities'] += [all_universities[entry]['name']]

def output_as_csv(content):
    # write gathered_facts to csv file using the Keys as the header/title
    with open('output_file.csv', 'w') as f: 
        w = csv.DictWriter(f, content.keys())
        w.writeheader()
        w.writerow(content)

### Main execution

# initiate the dictionary that will hold all future gathered facts
gathered_facts = {}

# get a city name from user
gathered_facts['city_name'] = input("Enter a City Name: ")

# populate gathered_facts dictionary
get_city_info(gathered_facts['city_name'])
get_forecast(gathered_facts['lat'],gathered_facts['long'])
get_current_covid_cases(gathered_facts['country'])
get_random_universities(gathered_facts['country'])

# write csv file
output_as_csv(gathered_facts)

#pretty print
print("Gathered Facts: ")
pprint(gathered_facts)