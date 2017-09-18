**PRACTICA 0**

#**Creación de par de claves y subida de clave a GitHub**
ssh-keygen -t rsa -C "carliyostole@gmail.com"

Con esto tenemos nuestra clave pública creada, entonces ingresamos a Github, y en la sección Settings elegimos la opción SSH Keys e ingresamos.

Hacemos click en el botón Add SSH Key.

En el campo Key pegamos el contenido del archivo id_rsa.pub
Y luego hacemos click en el bóton Add Key, nos pedirá nuestra contraseña de Github para validar y listo.


A continuación clonamos el directorio:
git clone https://github.com/carlillostole/proyectoIV17-18

#**Realizamos las tareas de commit y close#**

git add README.md

git commit -m "Archivo README actualizado close #1"
[master e3f74fc] Archivo README actualizado close #1
 1 file changed, 2 insertions(+)
 
git push origin master

#**Creamos hito0**

git checkout -b hito0

git push origin hito0

git branch
