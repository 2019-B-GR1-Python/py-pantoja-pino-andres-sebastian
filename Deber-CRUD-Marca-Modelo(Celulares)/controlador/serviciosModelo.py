from servicios import Servicios
class ServiciosModelo(Servicios):
    def __init__(self, nombre_archivo = "modelos.json"):
        super().__init__(nombre_archivo)

    
    def actualizar(self, dato_nuevo):
        indice_dato = self.buscar("id", dato_nuevo["id"])
        if indice_dato == -1:
            return "No se ha encontrado el elemento"
        else:
            self.datos[indice_dato]["id"] = dato_nuevo["id"]
            self.datos[indice_dato]["nombre"] = dato_nuevo["nombre"]
            self.datos[indice_dato]["color"] = dato_nuevo["color"]
            self.datos[indice_dato]["anio_salida"] = dato_nuevo["anio_salida"]
            self.datos[indice_dato]["precio"] = dato_nuevo["precio"]
            self.datos[indice_dato]["idMarca"] = dato_nuevo["idMarca"]
            self.archivo.escribir(self.nombre_archivo, self.datos)
            return f"Se ha modificado el elemento {self.datos[indice_dato]}"

    def marca_eliminada(self, idMarca):
        while True:
            indice_dato = self.buscar("idMarca", idMarca)
            if indice_dato == -1:
                break
            else:
                self.datos.pop(indice_dato)


