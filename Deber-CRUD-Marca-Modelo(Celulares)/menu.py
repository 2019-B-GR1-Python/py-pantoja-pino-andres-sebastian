from serviciosModelo import ServiciosModelo
from serviciosMarcas import ServiciosMarcas
class Menu:
    modelo_servicios = ServiciosModelo()
    marca_servicios = ServiciosMarcas()
    def menu_inicial(self):
        print("Bienvenido!" + "\n" + "Gestion de: " + "\n" + "1. Marcas" 
        + "\n" + "2. Modelos" + "\n" + "3. Salir" )
        entrada = self.pedir_entrada()
        if(entrada == "1"):
            self.gestion_marcas()
        elif(entrada == "2"):
            self.gestion_modelos()
        elif(entrada == "3"): 
            print("Adios!")
            exit(0)
        else:
            print("Ingrese una opción correcta")
            self.menu_inicial()

    def pedir_entrada(self):
        return input("Ingrese el número de la opcion seleccionada\n") 

    def gestion_marcas(self):
        
        
        print("Gestion de Marcas.\n" + "1. Crear\n" + "2. Mostrar todos\n" + "3. Buscar por ID\n" + "4. Buscar por Nombre\n" + "5. Actualizar\n" + 
        "6. Eliminar\n" + "7. Salir\n")
        entrada = self.pedir_entrada()

        if entrada == "1":
            self.entrada_Marcas()
            self.gestion_marcas()
        
        elif entrada == "2":
            respuesta = self.marca_servicios.mostrar_datos()
            print(respuesta)
            self.gestion_marcas()
            

        elif entrada == "3":
            # llamar a buscar id
            try:
                entrada = int(input("Ingrese el ID a buscar: "))
            except ValueError:
                print("El ID no es valido.")
            respuesta = self.marca_servicios.mostrar_uno_id(int(entrada))
            print(respuesta)
            self.gestion_marcas()
            

        elif entrada == "4":
            # llamar a buscar nombre
            entrada = input("Ingrese el NOMBRE a buscar: ")
            respuesta = self.marca_servicios.mostrar_uno_nombre(entrada)
            print(respuesta)
            self.gestion_marcas()
        
        elif entrada == "5":
            self.actualizacion_Marcas()
            self.gestion_marcas()

        elif entrada == "6":
            # llamar a eliminar
            entrada = input("Ingrese el ID a eliminar: ")
            respuesta = self.marca_servicios.eliminar(int(entrada))
            self.modelo_servicios.marca_eliminada(int(entrada))
            print(respuesta)
            self.gestion_marcas()
        
        elif entrada == "7":
            self.menu_inicial()
        
        else:
            print("Ingrese una opcion correcta")
            self.gestion_marcas()

    def gestion_modelos(self):
        
        
        print("Gestion de Modelos.\n" + "1. Crear\n" + "2. Mostrar todos\n" + "3. Buscar por ID\n" + "4. Buscar por Nombre\n" + "5. Actualizar\n" + 
        "6. Eliminar\n" + "7. Salir\n")
        entrada = self.pedir_entrada()

        if entrada == "1":
            self.entrada_Modelos()
            self.gestion_modelos()
        
        elif entrada == "2":
            respuesta = self.modelo_servicios.mostrar_datos()
            print(respuesta)
            self.gestion_modelos()
            

        elif entrada == "3":
            # llamar a buscar id
            try:
                entrada = int(input("Ingrese el ID a buscar: "))
            except ValueError:
                print("El ID no es valido.")
            respuesta = self.modelo_servicios.mostrar_uno_id(int(entrada))
            print(respuesta)
            self.gestion_marcas()
            

        elif entrada == "4":
            # llamar a buscar nombre
            entrada = input("Ingrese el NOMBRE a buscar: ")
            respuesta = self.modelo_servicios.mostrar_uno_nombre(entrada)
            print(respuesta)
            self.gestion_modelos()
        
        elif entrada == "5":
            self.actualizacion_Modelos()
            self.gestion_modelos()

        elif entrada == "6":
            # llamar a eliminar
            entrada = input("Ingrese el ID a eliminar: ")
            respuesta = self.modelo_servicios.eliminar(int(entrada))
            print(respuesta)
            self.gestion_modelos()
        
        elif entrada == "7":
            self.menu_inicial()
        
        else:
            print("Ingrese una opcion correcta")
            self.gestion_modelos()




    def entrada_Marcas(self):
        nombre = input("Ingrese el nombre: ")
        pais_origen = input("Ingrese el pais de origen: ")
        anio_fundacion = input("Ingrese el anio de fundacion: ")
        dispositivos_vendidos = input("Ingrese la cantidad de dispositivos vendidos: ")
        dato_ingresar = {
            "id" : 0,
            "nombre" : nombre,
            "pais_origen" : pais_origen,
            "anio_fundacion" : anio_fundacion,
            "dispositivos_vendidos" : dispositivos_vendidos
        }
        respuesta = self.marca_servicios.insertar(dato_ingresar)
        print(respuesta)

    def actualizacion_Marcas(self):
        id = input("Ingrese el ID del elemento a modificar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        pais_origen = input("Ingrese el nuevo pais de origen: ")
        anio_fundacion = input("Ingrese el nuevo anio de fundacion: ")
        dispositivos_vendidos = input("Ingrese la nueva cantidad de dispositivos vendidos: ")
        dato_actualizar = {
            "id" : id,
            "nombre" : nombre,
            "pais_origen" : pais_origen,
            "anio_fundacion" : anio_fundacion,
            "dispositivos_vendidos" : dispositivos_vendidos
        }
        respuesta = self.marca_servicios.actualizar(dato_actualizar)
        print(respuesta)
        

    
    def entrada_Modelos(self):
        nombre = input("Ingrese el nombre: ")
        color = input("Ingrese el color: ")
        anio_salida = input("Ingrese el anio de salida: ")
        precio = input("Ingrese el precio: ")
        dato_ingresar = {
            "id" : 0,
            "nombre" : nombre,
            "color" : color,
            "anio_salida" : anio_salida,
            "precio" : precio
        }
        respuesta = self.modelo_servicios.insertar(dato_ingresar)
        print(respuesta)

    def actualizacion_Modelos(self):
        id = input("Ingrese el ID del elemento a modificar: ")
        nombre = input("Ingrese el nombre: ")
        color = input("Ingrese el color: ")
        anio_salida = input("Ingrese el anio de salida: ")
        precio = input("Ingrese el precio: ")
        dato_ingresar = {
            "id" : id,
            "nombre" : nombre,
            "color" : color,
            "anio_salida" : anio_salida,
            "precio" : precio
        }
        respuesta = self.modelo_servicios.insertar(dato_ingresar)
        print(respuesta)
menu = Menu()
menu.menu_inicial()