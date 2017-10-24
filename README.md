
# The WeatherBOT - Proyecto Infraestructura Virtual 2017-2018 -  Grado en Ingeniería Informática

[![Build Status](https://travis-ci.org/carlillostole/proyectoIV17-18.svg?branch=master)](https://travis-ci.org/carlillostole/proyectoIV17-18)

## Objetivo

Mostrar sin necesidad de salir de Telegram y en cuestión de segundos, el tiempo actual de una ciudad.

## Descripción

Uso de un bot de Telegram para obtener información meteorológica de una ciudad determinada introducida. El bot va a estar alojado junto a una base de datos en un servidor en la nube ya sea en **Azure**, **Cloud9**, **Amazon web services**, etc.


## Más información

-	El usuario deberá tener Telegram para que se le envíe el pronóstico.
-	El bot estará online todo el tiempo.
-	Recopilará la información de forma autónoma.

## Servicios

-	Servidor de Base de Datos para el contenido del bot.
-	Servidor de Base de Datos para almacenar los usuarios que tenemos.

## Herramientas

-	API de Telegram para la realización del bot.
-	API OpenWeatherMap.
-	Lenguaje Python.

## Automatización, Make

Se ha creado un archivo Makefile para automatizar la creación del proyecto y realizar algun test de la aplicación.[make](https://github.com/carlillostole/proyectoIV17-18/blob/master/Makefile)

## Integración continua

El sistema de integración continua comprueba de forma continua que cada cambio realizado al repositorio, siga funcionando correctamente.

-	[Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **.travis.yml**. Mi archivo [.travis.yml](https://github.com/carlillostole/proyectoIV17-18/blob/master/.travis.yml)

## Despliegue en un PaaS

Se ha realizado el despliegue de la aplicación en Heroku. He elegido este PasS porque considero que ofrece buenos servicios, una buena interfaz y es fácil de usar.

Para llevar a cabo el despliegue tenemos que crear los siguientes ficheros: **Procfile**, **runtime.txt** y **requirements.txt**.

-	El fichero [Procfile](https://github.com/carlillostole/proyectoIV17-18/blob/master/Procfile) sirve para que Heroku ejecute el BOT. El archivo debe estar situado en la raíz del repositorio., para que lo identifique. NOTA:sin extensión.
-	El fichero [runtime.txt](https://github.com/carlillostole/proyectoIV17-18/blob/master/runtime.txt) indica la versión de python a utilizar.
-	El archivo [requirements.txt](https://github.com/carlillostole/proyectoIV17-18/blob/master/requirements.txt) sirve para que Heroku conozca las dependencias. Tiene extensión .txt y debe estar en la raíz del repositorio.

Este es el bot ya desplegado: [https://theweatherbot1718.herokuapp.com/](https://telegram.me/carlillostole_weatherBot).
También podemos buscar el nombre en TELEGRAM con el nombre: **@TheWeatherBOT**

### Configuración realizada

En primer lugar nos descargamos la linea de comandos de Heroku utilizando la orden:

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

```
Para autentificarnos en Heroku utilizamos `heroku login` y nos pedirá que introduzcamos **Email** y **Contraseña**

### Implementar aplicación

Para crear una aplicación en Heroku se utiliza el siguiente comando:

```
 heroku apps:create --region eu NOMBRE_APP

```

Una vez realizados todos estos pasos, la aplicación queda desplegada y configurada correctamente:

![1](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/herokudespligue.png?raw=true)
