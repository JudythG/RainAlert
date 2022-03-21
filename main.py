import requests
import os

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
exclude = "current,minutely,daily,alerts"

parameters = {
    "lat": -3.493074,
    "lon": -60.840861,
    "appid": api_key,
    "exclude": exclude,
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

hourly_weather_slice = response.json()['hourly'][:12]
bring_umbrella = False
for hourly_weather in hourly_weather_slice:
    if hourly_weather['weather'][0]['id'] < 700:
        bring_umbrella = True
        break
if bring_umbrella:
    print("Bring umbrella")

