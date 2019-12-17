# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:51:17 2019

@author: Andres
"""

import pandas as pd


path_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data.pickle"
path_entero_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data_entero.pickle" 
df = pd.read_pickle(path_guardado)
df2 = pd.read_pickle(path_entero_guardado)

##Obtener los artistas
serie_artistas_repetidos = df2["artist"]

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
son_blake = df2['artist'] == 'Blake, William'
df_blake = df2[son_blake]
obras_blake = df2[son_blake]['title']
blake_unicos = pd.unique(obras_blake)































