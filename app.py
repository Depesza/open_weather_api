import os
import requests
from sys import argv

OPEN_WEATHER_API_KEY = os.environ['OPEN_WEATHER_API_KEY']


def get_weather_based_on_location(city):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={OPEN_WEATHER_API_KEY}&units=metric')
        r.raise_for_status()
        temperature = r.json()['main']['temp']
        print(f'{temperature}°C')
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print('Please make sure you are entering the correct name of the city.')
        else:
            print('Sorry, something went wrong.')


get_weather_based_on_location(argv[1])
