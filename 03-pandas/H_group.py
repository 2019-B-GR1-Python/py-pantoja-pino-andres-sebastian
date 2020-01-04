# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:22 2020

@author: Andres
"""

import pandas as pd
import math
import numpy as np
path_entero_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data_entero.pickle" 

df = pd.read_pickle(path_entero_guardado)

seccion_df = df.iloc[49980:50019, :].copy()

df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)

for columna_grupada,df_completo in df_agrupado:
    print(columna_grupada)
    print(df_completo)
    print(type(columna_grupada))
    print(type(df_completo))
    
# Contar valores de la colmna
a = seccion_df['units'].value_counts()
# Verificar si esta vacía 
a.empty

    
def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty):
        return series;
    else:
        if(tipo == 'promedio'):
            suma = 0
            promedio = 0
            cantidad = 0
            for valor_serie in series:
                if(isinstance(valor_serie, str)):
                    valor = int(valor_serie)
                    suma = suma + valor
                    cantidad = cantidad + 1
                else:
                    pass
            promedio = suma / cantidad
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        
        elif(tipo == 'moda'):
            series_valores_llenos = series.fillna(lista_valores.index[0])
            return series_valores_llenos


def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'moda')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'moda')
        lista_df.append(copia)
    
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores
        
        
        
df_valores_llenos = transformar_df(seccion_df)
        
        
        
        
        
        
        
        
        
        
        
        
        