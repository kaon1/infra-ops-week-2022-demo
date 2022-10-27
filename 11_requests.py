# example script to grab random cat fact from public api endpoint
# use requests library get function
import requests

website_result = requests.get("https://catfact.ninja/fact")

print(website_result.text)
