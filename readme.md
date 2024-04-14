# Weather API
This is a web application written in python, use it to present the weather forecast of the next week.

## How to install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements on your virtual environment.

```bash
pip install -r requirements.txt
```


## How To Run

The weather.py file contains app and routes, so make sure to run this file in order to start the application.

## Data

On the main route when invoking a search, aka POST request, the input from the user is transfered to the get_data function and gets the coordinates from openweatherapi, procceeds to call the get_weather function that gets the temperatures and humidity from api.open-meteo and returns a list of 7 days with the forecast of each day.
Then, the result is displayed in a box for each day to the user using jinja on the HTML index page.


## Error handling

In case the user inserts an invalid city, an error page will be displayed to inform the user that this was a bad request, and give him the option to go back to the index/main page and search again.

## Functions

```python
from back import get_data

weather_data =get_data(city_input)
# takes as input the city the user inserted;
# returns a dictionary containing country, city and forecast = get_weather(lon,lat).

get_weather(lon,lat)
#takes as input lon and lat coordinates.
# returns to forecast a list containing 7 days where each day is a
dictionary that contain it's date, name, temperature at morning,
temperature at evening and humidity.
```

## References
[Jinja](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation)
[OpenWeatherMap](https://openweathermap.org/current)
[Open-Meteo](https://open-meteo.com/en/docs/)
[Flask](https://flask.palletsprojects.com/en/3.0.x/)
