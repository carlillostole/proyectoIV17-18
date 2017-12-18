# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def InstalarApp():
	""" Función para descargar el bot del repositorio. """
	# Descargamos el repositorio
	run('git clone https://github.com/carlillostole/proyectoIV17-18')

	# Instalamos pip3	
	run('sudo apt-get install -y python3-pip')

	# Accedemos al repositorio e instalamos las dependencias
	run('cd proyectoIV17-18/ && pip3 install -r requirements.txt')

def BorrarApp():
	""" Función para borrar el repositorio. """
	# Borramos el repositorio
	run('sudo rm -rf ./proyectoIV17-18')

def IniciarApp():
	""" Función para iniciar la web. """
	# Importamos las variables globales
	with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"):
		# Iniciamos el servicio web
		run('cd ~/proyectoIV17-18/ && sudo -E python3 app.py',pty=False)

