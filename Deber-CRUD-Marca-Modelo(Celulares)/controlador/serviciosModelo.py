from controlador.servicios import Servicios
from controlador.serviciosMarcas import ServiciosMarcas
class ServiciosModelo(Servicios):
    servicios_Marcas = ServiciosMarcas()
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
            self.archivo.escribir(self.nombre_archivo, self.datos)
            return f"Se ha modificado el elemento {self.datos[indice_dato]}"

    def marca_eliminada(self, idMarca):
        while True:
            indice_dato = self.buscar("idMarca", idMarca)
            if indice_dato == -1:
                break
            else:
                self.datos.pop(indice_dato)

    def ingresar_modelo(self,dato_nuevo):
        try:
            id_Marca_buscar = int(dato_nuevo["idMarca"])
        except ValueError:
            return "El ID de la marca no es valido."
        idMarca = self.servicios_Marcas.buscar("id", id_Marca_buscar)
        if idMarca == -1:
            return f"No existe la marca con ID {id_Marca_buscar}"
        else:
            dato_nuevo["idMarca"] = id_Marca_buscar
            return self.insertar(dato_nuevo)


