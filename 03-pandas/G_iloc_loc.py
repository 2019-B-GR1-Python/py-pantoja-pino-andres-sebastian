# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:56 2019

@author: Andres
"""

import pandas as pd
path_entero_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data_entero.pickle" 

df2 = pd.read_pickle(path_entero_guardado)

primero = df2.loc[1035, 'artist']


df3 = df2.set_index('id')


















dic_nombres ={
        "nota1": {
                "Pepito": 7,
                "Juanita": 8,
                "Maria": 9
                },
                "disciplina": {
                        "Pepito": 5,
                "Juanita": 9,
                "Maria": 2
                        }
        }


df_nombres = pd.DataFrame(dic_nombres)

df_nombres.loc[0]
df_nombres.iloc[0]
df_nombres.loc["Pepito"]
df_nombres.iloc["Pepito"]



df_nombres.loc[['Pepito', 'Juanita'], ['nota1', 'disciplina']]
condicion_nota1 = df_nombres['nota1']>7
condicion_disciplina = df_nombres['disciplina']>7
 

df_nombres.loc[condicion_nota1]


notas_mayores_7 = df_nombres['nota1']>7 and df_nombres['disciplina']>7

df_nombres.loc['Maria','disciplina'] = 7



"""
Ejercicios:
    Subir disciplina de todos a 7,
    Subir las notas dee peipto a 10
    La disciplina va a bajar a 7 -> notas.loc[:, 'disciplina'] = 7
    Sacar promedio de notas
"""

df_notas = pd.DataFrame(dic_nombres)
df_notas.loc[df_notas['disciplina']<7, 'disciplina'] = 7
df_notas.loc['Pepito'] = 10
df_notas.loc[:,'disciplina'] = 7



