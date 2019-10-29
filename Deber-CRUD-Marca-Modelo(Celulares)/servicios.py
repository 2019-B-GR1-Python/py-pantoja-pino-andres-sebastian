from archivo import Archivo
class Servicios:
    datos = None
    archivo = Archivo()
    def insertar(self,dato_nuevo):
        datos = self.archivo.leer("marcas.json")
        dato_nuevo["id"] = self.calcular_id(datos)
        datos.append(dato_nuevo)
        self.archivo.escribir("marcas.json",datos)

    def calcular_id(self, datos):
        return datos[-1]["id"] + 1
    
    def mostrar_datos(self):
        print(self.archivo.leer("marcas.json"))



servicios = Servicios()
servicios.mostrar_datos()
servicios.insertar({
    "id": 10,
    "nombre": "Nombre",
    "pais_origen": "Pais",
    "dispositivos_vendidos": 1000,
    "anio_fundacion": 1999
})
servicios.mostrar_datos()
