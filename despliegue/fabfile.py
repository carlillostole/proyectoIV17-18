from fabric.api import *
import os

def descargar():
    run ('sudo rm -rf proyectoIV17-18')
    run ('sudo git clone https://github.com/carlillostole/proyectoIV17-18')

def detener():
    run ("sudo supervisorctl stop theweather")

def borrar():
    run ('sudo rm -rf proyectoIV17-18')

def instalar():
    run ('cd proyectoIV17-18 && make install')

def recargar():
    run("sudo supervisorctl reload")

def iniciar_supervisor():
    with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"):
        run('sudo supervisorctl start theweather')

def iniciar():
    with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"):
        run('cd proyectoIV17-18 && python app.py')
	
def iniciar_hup():
    with shell_env(TOKENBOT="454323731:AAHV_dXizf08VAkEzfMUgOKN9VaM5KCFExI"):
        run ('nohup python proyectoIV17-18/TheWeatherBOT/bot.py >& /dev/null &',pty=False)
