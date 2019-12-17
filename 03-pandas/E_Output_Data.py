# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:48 2019

@author: Andres
"""
import numpy as np
import pandas as pd
import sqlite3
path_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data.pickle"
path_entero_guardado = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data_entero.pickle" 
df = pd.read_pickle(path_guardado)
df2 = pd.read_pickle(path_entero_guardado)

# iloc permite copiar cierta seccion del dataframe
df_guardar = df2.iloc[49980:50019, :].copy()
# To excel
columnas = ['artist', 'title', 'year']
path_excel = 'mi_df.xlsx'
df_guardar.to_excel(path_excel, index = False, columns =columnas)

path_multiple = 'mi_df_multiple.xlsx'
writer = pd.ExcelWriter(path_multiple,
                        engine = 'xlsxwriter')
df_guardar.to_excel(writer, sheet_name = 'Primera')
df_guardar.to_excel(writer, sheet_name = 'Segunda',
                    index = False)
df_guardar.to_excel(writer, sheet_name = 'Tercera',
                    columns = columnas)

writer.save()









# Ejercicio 
# Contar los artistas de un dataframe y darle formato
numero_artistas = df_guardar['artist'].value_counts()

path_colores = 'mi_df_colores.xlsx'

writer_colores = pd.ExcelWriter(path_colores,
                                engine = 'xlsxwriter')
numero_artistas.to_excel(writer_colores, 
                      sheet_name = 'Artistas')

hoja_artistas = writer_colores.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(numero_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer_colores.save()







## Grafico
import xlsxwriter
df_grafico = df2.iloc[49980:50119, :].copy()
num_artistas = df_grafico['artist'].value_counts()
workbook = xlsxwriter.Workbook('grafico.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A1', num_artistas.index.array)
worksheet.write_column('B1', num_artistas.array)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$B$1:$B${}'.format(len(num_artistas.index)),
                  'categories': '=Sheet1!$A$1:$A${}'.format(len(num_artistas.index)),
                  'name': 'artistas',
                  'marker': {
                          'type': 'square',
                          'size': 8,
                          'border': {'color': 'black'},
                          'fill':   {'color': 'red'},
                          }})

# Insert the chart into the worksheet.
worksheet.insert_chart('D1', chart)

workbook.close()



###SQL
import sqlite3
with sqlite3.connect("C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//bdd_artist.db") 
as conexion:
    df_guardar.to_sql('py_artistas', conexion)



###JSON
df.to_json("C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artist.json")


##JSON en forma de tabla
df.to_json("C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artist_table.json",
           orient = 'table')










