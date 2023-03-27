import os

import requests
import json

city = input("enter  the name of thecity: ")

url = f"https://api.weatherapi.com/v1/current.json?key=c4fa2edc0d20474881e81333232703&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])

os.system("say 'The current weather in {city} is {w} degrees'")