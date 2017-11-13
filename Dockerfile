# Version sistema operativo
FROM ubuntu:17.10

# Autor
MAINTAINER Carlos Toledano Delgado <carliyostole@gmail.com>

#Actualizar Repositorio
RUN apt-get update

#Instalamos git y descargamos el repositorio
RUN sudo git clone https://github.com/carlillostole/proyectoIV17-18

#Instalamos python y pip por medio de nuestro Makefile
RUN apt-get install -y python-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

# Instalacion de las dependencias del proyecto
RUN cd proyectoIV17-18 && make install
