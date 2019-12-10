# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:43 2019

@author: Andres
"""

import pandas as pd
import os

# 1. Archivos de texto -- JSON, HTML XML
# 2. Archivos binarios 
# 3. Relational Databases
path = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data.csv"

df1 = pd.read_csv(path, nrows = 10)

columnas = ['id', 'artist', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df2 = pd.read_csv(path, nrows = 10, usecols = columnas)

df3 = pd.read_csv(path, nrows = 10, usecols = columnas, index_col = 'id')

path_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data.pickle"
df3.to_pickle(path_guardado)
df4 = pd.read_csv(path)
path_entero_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data_entero.pickle" 
df4.to_pickle(path_entero_guardado)

