from archivo import Archivo
from servicios import Servicios
class ServiciosMarcas(Servicios):
    def __init__(self, nombre_archivo = "marcas.json"):
        super().__init__(nombre_archivo)

    
    def actualizar(self, dato_nuevo):
        indice_dato = self.buscar("id", dato_nuevo["id"])
        if indice_dato == -1:
            return "No se ha enconttrado el elemento"
        else:    
            self.datos[indice_dato]["id"] = dato_nuevo["id"]
            self.datos[indice_dato]["nombre"] = dato_nuevo["nombre"]
            self.datos[indice_dato]["pais_origen"] = dato_nuevo["pais_origen"]
            self.datos[indice_dato]["anio_fundacion"] = dato_nuevo["anio_fundacion"]
            self.datos[indice_dato]["dispositivos_vendidos"] = dato_nuevo["dispositivos_vendidos"]
            self.archivo.escribir(self.nombre_archivo, self.datos)
            return f"Se ha modificado el elemento {self.datos[indice_dato]}"
