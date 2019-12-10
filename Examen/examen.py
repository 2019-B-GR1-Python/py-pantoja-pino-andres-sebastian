import numpy as np
import pandas as pd

# Ejercicio 2
respuesta2 = np.zeros(10)

# Ejercicio 3
respuesta3 = np.zeros(10)
respuesta3[5:10] = 1

#Ejercicio 4
respuesta4 = np.arange(50)
respuesta4 = respuesta4[::-1]

#Ejercicio 5
respuesta5 = np.arange(9).reshape(3,3)

#Ejercicio 6
arreglo = [1,2,0,0,4,0]
arreglo_np = np.array(arreglo)
no_es_cero = arreglo_np != 0  
arreglo_no_cero = arreglo_np[no_es_cero]

#Ejercicio 7
ejercicio7 = np.eye(3)

#Ejercicio 8
respuesta8 = np.random.rand(3,3,3)

#Ejercicio 9
respuesta9 = np.random.rand(10,10)
minimo = respuesta9.min()
maximo = respuesta9.max()

#Ejercicio 10 ***********

# Ejercicio 11
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_lista = pd.Series(mylist)
serie_arreglo = pd.Series(myarr)
serie_diccionario = pd.Series(mydict)

#Ejercicio 12 
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 

# Transformar la serie en dataframe y hacer una columna indice
df12 = pd.DataFrame(ser)
df12.index = df12[0]

# Ejercicio 13
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df13 = pd.DataFrame({'0': ser1, '1': ser2})

# Ejercicio 14
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
esta_a_y_b = ser1.isin(ser2)
elementos_a_no_b = ser1[~esta_a_y_b]

# Ejercicio 15
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
elementos_no_comunes = ser1[~ser1.isin(ser2)].append(ser2[~ser2.isin(ser1)])

# Ejercicio 16
ser = pd.Series(np.take(list('abcdefgh'),
                        np.random.randint(8, size=30)))
conteo_valores = ser.value_counts()

# Ejercicio 17
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
conteo_valores = ser.value_counts()

def cambiar_por_cero(valor):
    esta_en_2_mayores = valor == conteo_valores.index[0] or valor == conteo_valores.index[1]
    if ~esta_en_2_mayores:
        valor = 0
    return valor

ser.map(cambiar_por_cero)

#Ejercicio 18
ser = pd.Series(np.random.randint(1, 10, 35))
shape = (7,5)
df18 = pd.DataFrame(ser.values.reshape(shape))
#Ejercicio 19
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
respuesta19 = ser[pos]

#Ejercicio 20 
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df20 = pd.DataFrame(ser1)
# Agregar verticalmente (columnas)
df20[1] = ser2

# Agregar horizontalmente (fila)
df20.append(pd.Series(['a', 5]), ignore_index = True)

# Ejercicio 21 
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
df21 = pd.DataFrame({
        'frutas': frutas,
        'pesos': pesos})
df21.groupby(['frutas']).mean()

# Ejercicio 22
#Path del archivo
path = "C://Users//Andres//Desktop//PYTHON//py-pantoja-pino-andres-sebastian//03-pandas//data//artwork_data.csv"
#Columnas por leer
columnas = ['id', 'artist', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
df22 = pd.read_csv(path, usecols = columnas)

