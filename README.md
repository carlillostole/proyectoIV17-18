
# The WeatherBOT - Proyecto Infraestructura Virtual 2017-2018 -  Grado en Ingeniería Informática

[![Build Status](https://travis-ci.org/carlillostole/proyectoIV17-18.svg?branch=master)](https://travis-ci.org/carlillostole/proyectoIV17-18)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/apps/theweatherbot1718)

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

![Docker: OK](https://dockerbuildbadges.quelltext.eu/status.svg?organization=niccokunzmann&repository=dockerhub-build-status-image)

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

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

Este es el bot ya desplegado: [https://theweatherbot1718.herokuapp.com/](https://theweatherbot1718.herokuapp.com/).
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
Por último, lanzamos tanto el bot como el servicio web.

```
heroku ps:scale worker=1 --app theweatherbot1718

heroku ps:scale web=1 --app theweatherbot1718

```

Una vez realizados todos estos pasos, la aplicación queda desplegada y configurada correctamente:

![1](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/despliegue.png?raw=true)

### Servicio web FLASK

Para desplegar el servicio web en Heroku he utilizado Flask y Gunicorn.

Primero lo instalamos con los siguientes comandos:

```
pip install gunicorn flask

```

```
pip install Flask

```
Una vez instalado el microframework Flask y gunicorn, creamos un archivo app.py en el directorio principal del proyecto que se está realizando, con el siguiente contenido:

```
from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/status')
def status():
    data={"status":"OK"}
    return json.dumps(data)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

```

Esto lo que hace es devolver Status: OK cuando abramos la aplicación web en Heroku con la dirección /status,( https://theweatherbot1718.herokuapp.com/status ), demostrando que el servicio esta arrancado y ejecutándose correctamente, conjuntamente con el worker. Para ver la pagina principal basta con abrir el enlace en /. ( https://theweatherbot1718.herokuapp.com/ )

En la siguiente captura se muestra tanto el worker como la aplicación web funcionando en Heroku, con todas las configuraciones realizadas correctamente.

![3](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/herokutotal.png?raw=true)

![4](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/status.png?raw=true)

### Despliegue

Despliegue https://theweatherbot1718.herokuapp.com/

### Despliegue en Docker

Para poder desplegar nuestro proyecto en Docker, nos registramos y seguidamente enlazamos con el repositorio de GitHub. Necesitamos añadir a nuestro repositorio el archivo [Dockerfile](https://github.com/carlillostole/proyectoIV17-18/blob/master/Dockerfile) para que Docker construya la imagen.

Una vez creado el archivo, Docker comenzará a construir un contenedor con los comandos que se encuentran en el archivo.

Como resultado obtenemos el contenedor creado y su configuración realizada:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/docker2.png?raw=true)

Dentro de la web se crea un "Automated Build" sobre el repositorio de nuestro proyecto en github, lo cual, cada vez que hacemos un push a nuestro repositorio, se actualizará de forma automática.

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/docker3.png?raw=true)


Para descargar nuestro contenedor introducimos el siguiente comando:

```
sudo docker build -t proyectoiv17-18 ./

```
El uso de "sudo" puede traer problemas, no es recomendado utilizarlo, podemos seguir el siguiente tutorial proporcionado por el profesor por telegram:

[Tutorial](https://docs.docker.com/engine/installation/linux/linux-postinstall/)

Una vez descargada la imagen de Docker comprobamos que se encuentra correctamente con el comando:

```
docker images

```

DockerHub: https://hub.docker.com/r/carlillostole/proyectoiv17-18/

### Despliegue en Azure

El despliegue en Azure lo he realizado siguiendo estos pasos:

Primero he canjeado un cupón proporcionado por el profesor para poder desplegar el proyecto correctamente, agradecimientos a diegomrtnzg y msabierto.

Una vez canjeado seguimos, creamos una aplicación basada en linux:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/azure1.png?raw=true)

A continuación introducimos el nombre de la aplicación, la suscripción de Azure, un grupo de recursos, el plan de App Service y por último enlazamos el contenedor Docker con la imagen/etiqueta de mi DockerHub, y le damos a aceptar.

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/azure2.png?raw=true)

Una vez creado tenemos lo siguiente, con un enlace a la aplicación desplegada:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/azure3.png?raw=true)

Aplicación desplegada:

Página principal:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/azure4.png?raw=true)

Status:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/azure5.png?raw=true)

Para que cargue correctamente y no de error, debemos configurar el puerto en el archivo Dockerfile como muestra a continuación:

![6](https://github.com/carlillostole/proyectoIV17-18/blob/master/img/dockerpuerto.png?raw=true)

Por último enlace al despliegue:

Contenedor: https://proyectoiv1718.azurewebsites.net

### Despliegue en Zeit

De forma opcional he decidido desplegar mi proyecto también en Zeit.

Para instalarlo hay que introducir el comando:
```
npm install -g now
```

La primera vez que inicie now, le pedirá su dirección de correo electrónico para identificarlo. Simplemente haga clic en el correo electrónico que ha recibido, y se iniciará sesión automáticamente.
```
now login
```

Una vez logueado, simplemente basta con abrir un terminal en el directorio que está la aplicación que queremos desplegar e introducir el comando now y automáticamente se desplegara y se creará la imagen.

Pero en este caso como es un proyecto que se esta desarrollando en GitHub, introducimos el siguiente comando el cuál despliega el repositorio indicado de GitHub:
```
now carlillostole/proyectoIV17-18
```

Despliegue en Zeit https://carlillostole-proyectoiv17-18-kuaehaxept.now.sh/

### Despliegue en un IaaS

La aplicación con la que he venido trabajando se ha desplegado en Azure. He empleado Vagrant como herramienta para la creación de la máquina virtual en la cual se alojará nuestra aplicación, en mi caso el bot de Telegram. También contendrá Ansible para el aprovisionamiento y Fabric para instalar y poner el bot en ejecución.

Todos los ficheros nombrados anteriormente son los siguientes: [Vagranfile](https://github.com/carlillostole/proyectoIV17-18/blob/master/Vagrantfile) para crear la máquina virtual, [Playbook de Ansible](https://github.com/carlillostole/proyectoIV17-18/blob/master/provision/playbook.yml) para el aprovisionamiento, el fichero [Fabfile](https://github.com/carlillostole/proyectoIV17-18/blob/master/despliegue/fabfile.py) para acceder remotamente y, por último, el fichero [weather.conf](https://github.com/carlillostole/proyectoIV17-18/blob/master/weather.conf) para lanzar el bot con supervisor y se mantenga en uso aunque se cierre la terminal. Si no se quiere usar supervisor, se puede utilizar nohup, actúa de la misma manera.

Para crear la máquina virtual usaremos la siguiente orden:

```
sudo vagrant up --provider=azure
```
Una vez está instalada y lanzada la máquina virtual, ejecutaremos el bot usando Fabric con la orden:

```
fab -H nombremaquina@nombreDNSmv funcion
```

Con esto nuestro bot ya estaría funcionando perfectamente y listo para poder hablarle.

Despliegue final: maquinaiv.westeurope.cloudapp.azure.com

Ampliando documentación proyecto...
