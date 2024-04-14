import os
import requests
from datetime import datetime, timedelta
from datetime import date
from dotenv import load_dotenv  # used to get api key from .env file

dt = datetime.now().date()

day_of_week = [(dt + timedelta(days=i)).strftime('%A') for i in range(7)]


def get_data(city_input):
    load_dotenv()
    my_api = os.getenv('API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&appid={my_api}'
    try:
        req = requests.get(url)
    except:
        return "Bad API response!"

    if req.status_code == 200:  # request from api.openweathermap api is ok
        data = req.json()
        country = data['sys']['country']
        city = data['name']
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        forecast = get_weather(lon, lat)
        if forecast == "Bad API response!":
            return "Bad API response!"

        return {
            "country": country,
            "city": city,
            "forecast": forecast
        }

    return req.status_code


def get_weather(lon, lat):
    url = (f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&'
           f'hourly=temperature_2m,relative_humidity_2m&timezone=auto')
    try:
        req = requests.get(url)
    except:
        return "Bad API response!"
    if req.status_code == 200:  # request from api.open-meteo api is ok

        data = req.json()
        hourly_data = data['hourly']
        time = hourly_data['time']
        humidity = hourly_data['relative_humidity_2m']
        temperature = hourly_data['temperature_2m']
        counter_hours = 6
        counter_day = 0
        # week_list is a variable containing a list that will hold the value and requested information for each day
        week_list = []
        # run in a loop and assign values to from now till the next week, which is 24 * 7 = 168 hours
        while counter_hours < 168:
            day = {"date": time[counter_hours], "day_of_week": day_of_week[counter_day],
                   "temperature_m": temperature[counter_hours], "temperature_e": temperature[counter_hours+12],
                   "humidity": humidity[counter_hours]}
            week_list.append(day)
            counter_hours += 24
            counter_day += 1
        return week_list
    else:
        return req.status_code
