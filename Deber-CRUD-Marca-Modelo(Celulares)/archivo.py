import json
class Archivo:
    data = None
    archivo = None
    
    def leer(self, nombre_archivo):
        self.archivo = open(nombre_archivo, 'r+')
        self.data = json.load(self.archivo)  
        self.archivo.close()
        return self.data

    def escribir(self,nombre_archivo,datos):
        self.archivo = open(nombre_archivo, 'w+')
        self.archivo.write(json.dumps(datos))
        self.archivo.close()

archivo = Archivo()
print(archivo.leer("marcas.json"))