# -*- coding: utf-8 -*-
import requests
import click


@click.command()
@click.option('--city', prompt='Which city are you in?',
              help='The city you are currently in.')
@click.option('--country', prompt='Which country?',
              help='The country your city is in.')
def weather(city, country):
    """Simple program that returns the weather for user's location."""
    maps_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + ',+' + country + '&key=AIzaSyBN21B-HqvlyUhrTbU8pB3BnFou4Y9I1RE'
    maps_response = requests.get(maps_geocode_url)
    maps_data = maps_response.json()

    lat = maps_data['results'][0]['geometry']['location']['lat']
    lon = maps_data['results'][0]['geometry']['location']['lng']

    def getUnits(country):
        imperialCountries = ['US', 'BS', 'BZ', 'KY', 'PW']

        if country not in imperialCountries:
            units = 'metric'
        else:
            units = 'imperial'
        return units

    units = getUnits(country)

    weatherApiUrl = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + "&units=" + units + '&appid=3c9d8a5d7e5933ca3111985a3d756cbf'
    open_weather_response = requests.get(weatherApiUrl)
    weather_data = open_weather_response.json()
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    def unitLabel(units):
        if units == 'imperial':
            unitLabel = "°F"
        else:
            unitLabel = "°C"
        return unitLabel

    label = unitLabel(units)

    click.echo('The temperature over there is %s %s' % (temperature, label))
    click.echo('The weather can be described as %s' % description)


if __name__ == '__main__':
    weather()
