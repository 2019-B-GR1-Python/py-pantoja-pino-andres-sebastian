from archivo import Archivo
class Servicios:
    datos = None
    archivo = Archivo()
    nombre_archivo = None

    def __init__(self, nombre_de_archivo):
        self.nombre_archivo = nombre_de_archivo
        self.leer_datos()
        

    def leer_datos(self):
        self.datos = self.archivo.leer(self.nombre_archivo)
    
    def insertar(self,dato_nuevo):
        def calcular_id(datos):
            return datos[-1]["id"] + 1
        
        dato_nuevo["id"] = calcular_id(self.datos)
        self.datos.append(dato_nuevo)
        self.archivo.escribir(self.nombre_archivo,self.datos)
        self.leer_datos()
        return f"Se ha insertado el elemento {datos[-1]}"
    
    def mostrar_datos(self):
        return self.datos
    

    def buscar(self, parametro_busqueda, valor):
            indice = 0
            for dato in self.datos:
                if dato[parametro_busqueda] == valor: 
                    return indice
                indice = indice + 1
            return -1

    def mostrar_uno_nombre(self, nombre):
        indice_dato = self.buscar("nombre", nombre)
        if(indice_dato == -1):
            return "No se ha encontrado el dato"
        else:
            return self.datos[indice_dato]


    def mostrar_uno_id(self, id):
        indice_dato = self.buscar("id", id)
        if(indice_dato == -1):
            return "No se ha encontrado el dato"
        else:
            return self.datos[indice_dato]

    def eliminar(self, id):
        indice = self.buscar("id", id)
        if (indice == -1):
            return "Elemento no encontrado"
        else:
            elemento_eliminado = self.datos.pop(indice)
            self.archivo.escribir(self.nombre_archivo, self.datos)
            return f"Se ha eliminado el elemento {elemento_eliminado}"
    
    def actualizar(self, dato_nuevo):
        indice_dato = self.buscar("id", dato_nuevo["id"])
        self.datos[indice_dato]["id"] = dato_nuevo["id"]
        self.datos[indice_dato]["nombre"] = dato_nuevo["nombre"]
        self.datos[indice_dato]["pais_origen"] = dato_nuevo["pais_origen"]
        self.datos[indice_dato]["anio_fundacion"] = dato_nuevo["anio_fundacion"]
        self.datos[indice_dato]["dispositivos_vendidos"] = dato_nuevo["dispositivos_vendidos"]
        self.archivo.escribir(self.nombre_archivo, self.datos)
        return f"Se ha modificado el elemento {datos[indice_dato]}"
