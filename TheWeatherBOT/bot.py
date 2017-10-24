# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# # bot.py

import falcon
import sqlite3
import telebot
import telegram
import json
import traceback
import sys
import requests
import logging
import os
from weather import get_weather

from telegram.ext import CommandHandler
from telegram.ext import Updater
from wsgiref import simple_server

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
#WEATHER_URL = "http://api.openweathermap.org/data/2.5/find"


TOKEN = "454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI" 
#bot = telegram.Bot(token=TOKEN)
bot = telebot.TeleBot(TOKEN)




app = falcon.API()

# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text

    print("ID: " + str(id) + " MENSAJE: " + mensaje)



def mensaje_busqueda(mensaje):
    mensaje = ''.join(mensaje.split())
    ciudad=mensaje[0:3]
    return {'ciudad':ciudad }


# Método que utilizaremos para cuando se mande el comando de "start"
@bot.message_handler(commands=['start','hola'])
def start(message):
    bot.reply_to(message, "Bienvenido a tu bot de metereologia, introduce una ciudad porfavor:")
    
@bot.message_handler(commands=['tiempo'])
def tiempo_ciudad(m):
    """Función que envia la prediccion de la ciudad al usuario. """
    iconos = { '01d': "\xE2\x98\x80", '02d': "\xE2\x9B\x85", '03d':"\xE2\x98\x81",
    '04d': "\xE2\x98\x81",'09d':"\xE2\x98\x94" ,'10d':"\xE2\x98\x94" ,'11d': "\xE2\x9A\xA1" ,'13d': "\xE2\x9D\x84" ,'50d': "\xF0\x9F\x8C\x81" }
    
    message_id = m.message_id
    date = m.date
    text = m.text
    chat = m.chat
    chat_id = m.chat.id
    
    cid = m.chat.id # Obtenemos la id del usuario.
    mensaje = m.text[7:]
    resp = get_weather(mensaje)
    bot.send_message(cid, "Buscando el tiempo en "+ mensaje)


    if resp:
        icono = iconos.get(resp.icono,"\xE2\x98\x80")
        text = ("Actualmente: {} \n{}\nTemperatura: {} ºC\nHumedad: {}%\nPresión: {} hPa").format(
                icono,resp.desc, resp.temp, resp.humedad, resp.presion)
        bot.send_message(chat_id, text, message_id)
    else:
        bot.send_message(chat_id, 'No puedo encontrar información meteorológica para esa ubicación.', message_id)
    return
    


bot.polling(none_stop=True)  
while True: #Infinite loop 
    pass

#if __name__ == '__main__':
#     main()
    # httpd = simple_server.make_server('127.0.0.1', 8000, app)
    # httpd.serve_forever()
    
