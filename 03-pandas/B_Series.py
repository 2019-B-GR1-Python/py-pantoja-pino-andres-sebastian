# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:34 2019

@author: Andres
"""

import numpy as np
import pandas as pd

lista_numeros = [1, 2, 3, 4]
tupla_numeros = (1, 2, 3, 4)
np_numeros = np.array((1, 2, 3, 4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)
serie_d = pd.Series([
        True,
        False,
        12,
        112.321,
        "Andres",
        "1",
        None,
        (),
        [],
        {"nombre": "Andres"}])

serie_d[3]

lista_ciudades = ["Ambato",
                 "Cuenca",
                 "Loja",
                 "Quito"]
serie_ciudades = pd.Series(lista_ciudades, 
                           index=[
                                   "A",
                                   "C",
                                   "L",
                                   "Q"])


serie_ciudades["A"]
serie_ciudades[0]



valores_ciudad = {
        "Ibarra": 9500,
        "Guayaquil": 10000,
        "Cuanca": 7000,
        "Quito": 8000,
        "Loja": 3000}

serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad["Quito"]
serie_valor_ciudad[4]

ciudades_menores_5000 = serie_valor_ciudad < 5000

serie5 = serie_valor_ciudad[ciudades_menores_5000]


aumento_10_porciento = serie_valor_ciudad * 1.10

serie_valor_ciudad * 1.10
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)


respuesta_square = np.square(serie_valor_ciudad)

respuesta_sin = np.sin(serie_valor_ciudad)


ciudades_uno = pd.Series({
        "Montañita": 300,
        "Guayaquil": 10000,
        "Quito": 2000})


ciudades_dos = pd.Series({
        "Loja": 300,
        "Guayaquil": 10000})

total = ciudades_uno + ciudades_dos

ciudades_uno["Loja"] = 0
ciudades_dos["Quito"] = 0
ciudades_dos["Montañita"] = 0

ciudad_add = ciudades_uno.add(ciudades_dos)
ciudades_concatenadas = pd.concat([
        ciudades_uno,
        ciudades_dos])

ciudades_concatenadas_verified = pd.concat([
        ciudades_uno,
        ciudades_dos], verify_integrity = True)


ciudades_append = ciudades_uno.append(ciudades_dos, verify_integrity = True)


ciudades_uno.max()
pd.Series.max(ciudades_uno)
ciudades_uno.min()
pd.Series.min(ciudades_uno)

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2)
ciudades_uno.tail(2)
ciudades_uno.sort_values().head(2)
ciudades_uno.sort_values().tail(2)



ciudades_uno.sort_values()
ciudades_uno.sort_values(ascending = False)

