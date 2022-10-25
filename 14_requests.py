import requests

website_result = requests.get("https://catfact.ninja/fact")

print(website_result.text)
