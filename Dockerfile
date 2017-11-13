# Sistema operativo
FROM ubuntu:17.10

# Autor
MAINTAINER Carlos Toledano Delgado <carliyostole@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

# Instalacion 
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/carlillostole/proyectoIV17-18

#Instalar python
RUN sudo apt-get -y install python-dev
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get install -y build-essential
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

# Instalacion de las dependencias del proyecto
RUN cd proyectoIV17-18/ && make install
