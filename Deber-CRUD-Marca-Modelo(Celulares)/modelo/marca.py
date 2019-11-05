class Marca:
    id = None
    nombre = None
    pais_origen = None
    anio_fundacion = None
    dispositivos_vendidos = None

    def __init__(self, diccionario_marca):
        self.id = diccionario_marca.id
        self.pais_origen = diccionario_marca.pais_origen
        self.anio_fundacion = diccionario_marca.anio_fundacion
        self.dispositivos_vendidos = diccionario_marca.dispositivos_vendidos
        
