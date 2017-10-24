# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import requests
import logging

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

class Weather():
    
    def __init__(self, temp, humedad, presion, desc, icono):
        self.temp = temp
        self.humedad = humedad
        self.presion = presion
        self.desc = desc
        self.icono = icono
    
#def get_weather(latitude, longitude):
def get_weather(ciudad):

    params = {'q': ciudad, 'units': "metric", 'lang': "es", 'appid': "0b69f1e24c6a35d5c271c753177a1368"}
    result = requests.get(WEATHER_URL, params=params)
    try:
        data = result.json()
    except:
        logging.error('Weather API call failed: {}'.format(result.status_code))
        return None
        
    # Create the Weather object from the json data.
    temp = data['main']['temp']
    humedad = data['main']['humidity']
    presion = data['main']['pressure']
    desc = data['weather'][0]['main'] + ': ' + data['weather'][0]['description']
    icono = data['weather'][0]['icon'] 
    return Weather(temp, humedad, presion, desc, icono)