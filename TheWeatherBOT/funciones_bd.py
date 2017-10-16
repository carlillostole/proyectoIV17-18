#!/bin/usr/python
# -*- coding: utf-8 -*-

import sqlite3

def ciudades(consulta):
    db = sqlite3.connect('datosmeteo.db') # conectamos con la bd
    b = db.cursor()
    b.execute(consulta) # Obtenemos el resultado de la consulta
    resp = ""
    for r in b:
        # Mandamos un string con un formato válido.
        aux = str(r)
        pos1 = aux.find("'")
        pos2 = aux.find("'", len(aux)-3)
        final = ""
        for i in range(pos1+1, pos2):
            final += aux[i]
        resp += str(final) + "\n"

    # Cierre de conexión con la base de datos.
    b.close()
    db.close()
    return resp

def cuentaCiudades():
    """ Función que devuelve el total de actividades disponibles """
    # Conectamos con la base de datos
    db = sqlite3.connect('datosmeteo.db')
    b = db.cursor()
    b.execute("SELECT * FROM ciudades") # Obtenemos el resultado de la consulta
    total = 0
    # Obtenemos la cantidad de ciudades disponibles.
    for i in b:
        total += 1
    # Cerramos la base de datos
    b.close()
    db.close()
    return total

def insertar(ciudad, temperatura, humedad,presion):
    db = sqlite3.connect('datosmeteo.db')
    b = db.cursor()
    b.execute("INSERT INTO ciudades (ciudad, temperatura, humedad,presion) VALUES (?, ?, ?,?)", (ciudad, temperatura, humedad,presion))
    db.commit()
    b.close()
	#db.close()
