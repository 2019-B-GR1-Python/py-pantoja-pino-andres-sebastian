import pygame, sys
from pygame.locals import *
import time
from random import randint
import datetime
import json

class Comida:
    x = 0
    y = 0
    espacio = None
    
    def __init__(self, x, y, espacio):
        self.espacio = espacio
        self.x = x * self.espacio
        self.y = y * self.espacio

    def dibujar(self, superficie, imagen):
        superficie.blit(imagen, (self.x, self.y))
        
        
class Serpiente:
    x = [450]
    y = [250]
    paso = 16
    direccion = 0
    longitud = 3
    
    cuenta_maxima = 2
    cuenta = 0
    
    def __init__(self, longitud):
        self.longitud = longitud
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)
            
        self.x[1] = 1 * self.paso
        self.x[2] = 2 * self.paso
        
    
    def actualizar(self):
        self.cuenta = self.cuenta + 1
        if self.cuenta > self.cuenta_maxima:
            
            for i in range(self.longitud - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]
        
            
            if self.direccion == 0:
                self.x[0] = self.x[0] + self.paso
            if self.direccion == 1:
                self.x[0] = self.x[0] - self.paso
            if self.direccion == 2:
                self.y[0] = self.y[0] - self.paso
            if self.direccion == 3:
                self.y[0] = self.y[0] + self.paso
        
            self.cuenta = 0
            
            
    def mover_izquierda(self):
        if(self.direccion !=0):
            self.direccion = 1
        else:
            self.direccion = 0

    def mover_derecha(self):
        if(self.direccion !=1):
            self.direccion = 0
        else:
            self.direccion = 1
        
    def mover_arriba(self):
        if(self.direccion !=3):
            self.direccion = 2
        else:
            self.direccion = 3
        
    def mover_abajo(self):
        if(self.direccion !=2):
            self.direccion = 3
        else:
            self.direccion = 2

    def dibujar(self, superficie, imagen):
        for i in range(0, self.longitud):    
            superficie.blit(imagen, (self.x[i], self.y[i]))
        

class Colision:
    def hay_colision(self, x1, y1, x2, y2, box_size):
        if x1 + box_size >= x2 and x1 <= (x2 + box_size):
            if y1 + box_size >= y2 and y1 <= (y2 + box_size):
                return True
        return False
    

class Juego:
    largo_ventana = 500
    ancho_ventana = 900
    serpiente = None
    en_juego = None
    display = None
    imagen = None
    nombre_imagen = "serpiente.png"
    nombre_imagen_comida = "fruit.png"
    espacio_comida = 16
    imagen_comida = None
    comida = None
    puntaje = 0
    nombre_imagen_background ="snake_bg.png" 
    background = None
    font = None
    score_label = None
    user_label = None
    username = None
    label_size = 25
    comida_grande_activa = False
    comida_normal_obtenida = 0
    comida_grande = None
    nombre_imagen_comida_grande = "candy.png"
    imagen_comida_grande = None
    espacio_comida_grande = 32
    contador_comida_grande = 0
    tiempo_inicio = None
    tiempo_fin = None
    def __init__(self, username):
        self.en_juego = True
        self.serpiente = Serpiente(3)
        self.comida = Comida(
                10 ,
                10 ,
                self.espacio_comida)
        self.comida_grande = Comida(
                10,20 ,
                self.espacio_comida)
        self.colision = Colision()
        self.username = username
        self.tiempo_inicio = datetime.datetime.now()
        
        
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.ancho_ventana, self.largo_ventana), pygame.HWSURFACE)
        
        pygame.display.set_caption('Mi jueguito de snake')
        self.en_juego = True
        self.imagen = pygame.image.load(self.nombre_imagen).convert()
        self.imagen_comida = pygame.image.load(self.nombre_imagen_comida).convert()
        self.imagen_comida_grande = pygame.image.load(self.nombre_imagen_comida_grande).convert()
        self.background = pygame.image.load(self.nombre_imagen_background);
        self.font = pygame.font.SysFont("elephant", self.label_size)
        
        
    def espera(self):
        self.serpiente.actualizar()
        if(self.serpiente.x[0] >= self.ancho_ventana or
           self.serpiente.x[0] <= 0 or 
           self.serpiente.y[0] <= 0 or
           self.serpiente.y[0] >= self.largo_ventana) :
            self.en_juego = False
        
        if self.comida_grande_activa:
            for i in range(0, self.serpiente.longitud):
                if self.colision.hay_colision(
                        self.comida_grande.x,
                        self.comida_grande.y,
                        self.serpiente.x[i],
                        self.serpiente.y[i],
                        32):
                    self.puntaje += 5
                    self.serpiente.longitud = self.serpiente.longitud + 3
                    self.comida_grande_activa = False
                    self.contador_comida_grande = 0
                    self.comida_grande.x = randint(2, self.ancho_ventana - self.espacio_comida_grande) 
                    self.comida_grande.y = randint(2, self.largo_ventana - self.espacio_comida_grande) 
            
        
        for i in range(0, self.serpiente.longitud):
            if self.colision.hay_colision(
                    self.comida.x,
                    self.comida.y,
                    self.serpiente.x[i],
                    self.serpiente.y[i],
                    16):
                self.puntaje += 1
                self.comida_normal_obtenida += 1
                if(self.comida_normal_obtenida % 3 == 0):
                    self.comida_grande_activa = True
                self.comida.x = randint(2, self.ancho_ventana - self.espacio_comida) 
                self.comida.y = randint(2, self.largo_ventana - self.espacio_comida) 
                self.serpiente.longitud = self.serpiente.longitud + 1 
        
        
        for i in range(2, self.serpiente.longitud):
            if self.colision.hay_colision(
                    self.serpiente.x[0],
                    self.serpiente.y[0],
                    self.serpiente.x[i],
                    self.serpiente.y[i],
                    10):
                self.en_juego = False
        pass
    
        
    def on_event(self, event):
        if event.type == QUIT:
            self.en_juego = False
            
            
    def on_render(self):
        self.display.blit(self.background,(0,0))
        self.score_label = self.font.render("Score: " + str(self.puntaje), 1, (255,255,255))
        self.user_label = self.font.render(self.username, 1, (255,255,255))
        self.display.blit(self.score_label, (10,10))
        self.display.blit(self.user_label, (self.ancho_ventana-(len(self.username) * self.label_size),10))
        self.serpiente.dibujar(self.display, self.imagen)
        self.comida.dibujar(self.display, self.imagen_comida)
        if(self.comida_grande_activa):
            self.comida_grande.dibujar(self.display, self.imagen_comida_grande)
            self.contador_comida_grande +=1
        if(self.contador_comida_grande == 150):
            self.comida_grande_activa = False
            self.contador_comida_grande = 0
            self.comida_grande.x = randint(2, self.ancho_ventana - self.espacio_comida_grande) 
            self.comida_grande.y = randint(2, self.largo_ventana - self.espacio_comida_grande) 
        pygame.display.flip()
        
    def on_cleanup(self):
        self.tiempo_fin = datetime.datetime.now()
        data = {
                "tiempo_inicio": str(self.tiempo_inicio),
                "tiempo_fin": str(self.tiempo_fin),
                "username": self.username,
                "score": self.puntaje
                }
        with open("datos.txt", "a+", encoding = "utf-8") as archivo:
            json.dump(data, archivo, indent = 4)
        pygame.quit()
        pygame.display.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self.en_juego = False
            
        while(self.en_juego):
            pygame.event.pump()
            teclas = pygame.key.get_pressed()
            
            if (teclas[K_RIGHT]):
                self.serpiente.mover_derecha()
            
            if (teclas[K_LEFT]):
                self.serpiente.mover_izquierda()
                
            if (teclas[K_UP]):
                self.serpiente.mover_arriba()
                
            if (teclas[K_DOWN]):
                self.serpiente.mover_abajo()
                
            self.on_render()
            self.espera()
            time.sleep (50.0 / 1000.0);
            
        self.on_cleanup()
    
    
if __name__ == "__main__":
    juego =  Juego("Holi")
    juego.on_execute()