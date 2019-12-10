# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:39:45 2019

@author: Andres
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "C://Users//Andres//Desktop//PYTHON//titanic.csv"
columnas = ['Survived','Sex'];
# Pie chart de hombres y mujeres
df = pd.read_csv(path, usecols = columnas);
total = len(df)
numero_por_sexo = df['Sex'].value_counts();

promedios_por_sexo = numero_por_sexo.apply(lambda x: 100 * x / float(total))

labels = ['Hombres','Mujeres'];

fig1, ax1 = plt.subplots()
ax1.pie(promedios_por_sexo, labesl = labels, autopct = '%1.4f%%', shadow = True, startangle = 180)
ax1.axis('equal')
plt.show()

#
columnas = ['Survived','Sex'];
df1 = pd.read_csv(path, usecols = columnas);
total = len(df1)
df_mujeres = df1[df1['Sex'] == 'female']
supervivencia_mujeres = df_mujeres['Survived'].value_counts().apply(lambda x: 100 *x / float(len(df_mujeres)))
df_hombres = df1[df1['Sex'] == 'male']
supervivencia_hombres = df_hombres['Survived'].value_counts().apply(lambda x: 100 * x / float(len(df_hombres)));

values = np.array([supervivencia_hombres.array, supervivencia_mujeres.array])

fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(values.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(values.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()





columnas = ['Age','Sex'];
df2 = pd.read_csv(path, usecols = columnas);
df2 = df2.round()
media = df2['Age'].mean()
media = round(media)
df2 = df2.fillna(media)

df_mujeres = df2[df2['Sex'] == 'female']
edades_mujeres = df_mujeres['Age'].value_counts()
df_hombres = df2[df2['Sex'] == 'male']
edades_hombres = df_hombres['Age'].value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Cantidad de pasajeros por edad y sexo')
ax1.bar(edades_hombres.index, edades_hombres, align='center', alpha=0.5)
ax2.bar(edades_mujeres.index, edades_mujeres, align='center', alpha=0.5)


columnas = ['Age','Survived'];
df3 = pd.read_csv(path, usecols = columnas);
df3 = df3.round()
df3 = df3.fillna(round(df3['Age'].mean()))
sobrevivientes_edad = df3[df3['Survived'] == 1]['Age'].value_counts()
fig, ax = plt.subplots()
ax.plot(sobrevivientes_edad.index, sobrevivientes_edad, 'bo') 



columnas = ['Embarked']
embarked = pd.read_csv(path, usecols = columnas)
cantidad_por_puesto = embarked['Embarked'].value_counts()
fig, ax = plt.subplots()
ax.bar(
       ['Southampton', 'Cherbourg', 'Queenstown'],
       cantidad_por_puesto)


columnas = ['Fare', 'Age']
fare_age = pd.read_csv(path, usecols = columnas)
fare_age = fare_age.fillna(round(fare_age['Age'].mean()))
colors = (0,0,0)
area = np.pi*3

plt.scatter(fare_age['Age'], fare_age['Fare'], s=area, alpha=0.5)
plt.title('Precio de boleto por edad')
plt.xlabel('Edad')
plt.ylabel('Precio')
plt.show()


columnas = ['Fare', 'Pclass']
fare_class = pd.read_csv(path, usecols = columnas)
first = fare_class[fare_class['Pclass'] == 1]['Fare'].unique()
second = fare_class[fare_class['Pclass'] == 2]['Fare'].unique()
third = fare_class[fare_class['Pclass'] == 3]['Fare'].unique()
valores = np.array([first, second, third])
plt.imshow(valores,interpolation='none',cmap=plt.cm.jet,origin='lower') 
