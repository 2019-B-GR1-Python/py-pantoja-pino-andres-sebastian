class Menu:
    def menu_inicial(self):
        print("Bienvenido!" + "\n" + "Gestion de: " + "\n" + "1. Marcas" 
        + "\n" + "2. Modelos" + "\n" + "3. Salir" )
        entrada = input("Ingrese el número de la opcion por seleccionada\n") 
        if(entrada == "1"):
            print("Gestion de marcas")
        elif(entrada == "2"):
            print ("Gestion de modelos")
        elif(entrada == "3"): 
            print("Adios!")
            exit(0)
        else:
            print("Ingrese una opción correcta")
            self.menu_inicial()


menu = Menu()
menu.menu_inicial()