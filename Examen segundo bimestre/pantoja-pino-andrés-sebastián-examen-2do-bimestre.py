# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:35:15 2020

@author: Andres
"""

import pandas as pd
import numpy as np
from datetime import date


# Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros


arreglo = np.random.randint(0, 10, 60).reshape(10,6)

df1 = pd.DataFrame(arreglo)

cinco_primeros = df1.head()

cinco_ultimos = df1.tail()

# Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

arreglo2 = np.random.randint(0,10,24).reshape(6, 4)
columnas = ['A', 'B', 'C', 'D']
indices = [date.today().strftime("%Y-%m-%d"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y")
        ]
df2 = pd.DataFrame(
        arreglo2,
        columns = columnas,
        index = indices
        )

#Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores
arreglo3 = np.random.randint(0,10,60).reshape(10, 6)
df3 = pd.DataFrame(arreglo3)

columnas_df3 = df3.columns.values

valores = df3.values


# Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

arreglo4 = np.random.randint(0,10,60).reshape(10, 6)
df4 = pd.DataFrame(arreglo4)

descripcion_df = df4.describe()

# Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

arreglo5 = np.random.randint(0,10,60).reshape(10, 6)
df5 = pd.DataFrame(arreglo5)

df5_transpuesto = df5.transpose()

# Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente *****


arreglo6 = np.random.randint(0,10,60).reshape(10, 6)
df6 = pd.DataFrame(arreglo6)

df6_ascendente = df6.apply(lambda x: x.sort_values().values)
df6_descendente = df6.apply(lambda x: x.sort_values(ascending = False).values)


# Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

arreglo7 = np.random.randint(1,10,60).reshape(10, 6)
df7 = pd.DataFrame(arreglo7)

mayores_a_7 = df7 > 7

df_mayores_7 = df7[mayores_a_7]


# Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0

arreglo8 = np.random.randint(1,10,60).reshape(10, 6)
df8 = pd.DataFrame(arreglo8)
mayores_a_5 = df8 > 5
df8_nan = df7[mayores_a_5]

df8_con_0 = df8_nan.fillna(0)


# Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

arreglo9 = np.random.randint(0,10,60).reshape(10, 6)
df9 = pd.DataFrame(arreglo9)

media = df9.mean()
mediana = df9.median()
promedio = df9.mean()


# Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

arreglo10_1 = np.random.randint(1,10,60).reshape(10, 6)
df10_1 = pd.DataFrame(arreglo10_1)
arreglo10_2 = np.random.randint(1,10,60).reshape(10, 6)
df10_2 = pd.DataFrame(arreglo10_2)

df10_final = df10_1.append(df10_2)



# Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

s_arr = pd.util.testing.rands_array(3, 60).reshape(10,6)
df11 = pd.DataFrame(s_arr)

df11_final = pd.DataFrame(df11[0] + df11[1])
df11_final[1] = df11[2] + df11[3]
df11_final[2] = df11[4] + df11[5]
        
        
#Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna
arreglo12 = np.random.randint(0,10,60).reshape(10, 6)
df12 = pd.DataFrame(arreglo12)

for column in df12.columns:
    print("Columna " + str(column))
    print(df12[column].value_counts())
    
# Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C
    
arreglo13 = np.random.randint(1,10,30).reshape(10, 3)
df13 = pd.DataFrame(arreglo13, columns = ['A', 'B', 'C'])
print(df13['A'][0])
resultados = []
for index in df13.index:
    resultados.append((df13['A'][index] * df13['B'][index]) / df13['C'][index] )
    
print(resultados)

df13['Resultados'] = resultados
    
