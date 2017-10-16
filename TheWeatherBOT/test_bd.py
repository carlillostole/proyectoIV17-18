#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import funciones_bd

class TestStringMethods(unittest.TestCase):

    def test_existe_ciudades(self):
        """ Test que comprueba si hay ciudades disponibles. """
        total = funciones_bd.cuentaCiudades()
        self.assertNotEqual(total, 0)

    def test_nombre_ciudad(self):
        """ Test que devuelve true si hay una ciudad con una temperatura concreta. """
        ciudad_disponible = funciones_bd.ciudades("SELECT * FROM ciudades WHERE temperatura='10'")
        self.assertIsNotNone(ciudad_disponible)

    def test_temperatura_ciudad(self):
        """ Test que devuelve true si el nombre de la ciudad coincide"""
        nombre = funciones_bd.ciudades("SELECT ciudad FROM ciudades WHERE ciudad='granada'")
        self.assertEqual(nombre, "granada\n")


if __name__ == '__main__':
	unittest.main()
