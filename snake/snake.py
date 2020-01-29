import pygame, sys
from pygame.locals import *
import time
from random import randint

class Comida:
    x = 0
    y = 0
    paso = 44
    
    def __init__(self, x, y):
        self.x = x * self.paso
        self.y = y * self.paso

    def dibujar(self, superficie, imagen):
        superficie.blit(imagen, (self.x, self.y))
        
        
class Serpiente:
    x = [0]
    y = [0]
    paso = 44
    direccion = 0
    longitud = 3
    
    cuenta_maxima = 2
    cuenta = 0
    
    def __init__(self, longitud):
        self.longitud = longitud
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)
            
        self.x[1] = 1 * 44
        self.x[2] = 2 * 44
        
    
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
                self.y[0] = self.y[0] + self.paso
            if self.direccion == 3:
                self.y[0] = self.y[0] - self.paso
        
            self.cuenta = 0
            
            
    def mover_izquierda(self):
        self.direccion = 0

    def mover_derecha(self):
        self.direccion = 1
        
    def mover_arriba(self):
        self.direccion = 2
        
    def mover_abajo(self):
        self.direccion = 3

    def dibujar(self, superficie, imagen):
        for i in range(0, self.longitud):    
            superficie.blit(imagen, (self.x[i], self.y[i]))
        

class Colision:
    def hay_colision(self, x1, y1, x2, y2, box_size):
        if x1 >= x2 and x1 <= (x2 + box_size):
            if y1 >= y2 and y1 <= (y2 + box_size):
                return True
        return False
    

class Juego:
    largo_ventana = 800
    ancho_ventana = 600
    serpiente = None
    en_juego = None
    display = None
    imagen = None
    nombre_imagen = "serpiente.png"
    imagen_comida = None
    comida = None
    def __init__(self):
        self.en_juego = True
        self.serpiente = Serpiente(3)
        self.comida = Comida(5, 5)
        self.colision = Colision()
        
        
        
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.ancho_ventana, self.largo_ventana), pygame.HWSURFACE)
        
        pygame.display.set_caption('Mi juiguito de snake')
        self.en_juego = True
        self.imagen = pygame.image.load(self.nombre_imagen).convert()
        self.imagen_comida = pygame.image.load(self.nombre_imagen).convert()
        
        
    def espera(self):
        self.serpiente.actualizar()
        
        for i in range(0, self.serpiente.longitud):
            if self.colision.hay_colision(
                    self.comida.x,
                    self.comida.y,
                    self.serpiente.x[i],
                    self.serpiente.y[i],
                    44):
                self.comida.x = randint(2, 9) * 44
                self.comida.y = randint(2, 9) * 44
                self.serpiente.longitud = self.serpiente.longitud + 1 
        
        
        for i in range(2, self.serpiente.longitud):
            if self.colision.hay_colision(
                    self.serpiente.x[0],
                    self.serpiente.y[0],
                    self.serpiente.x[i],
                    self.serpiente.y[i],
                    40):
                print("Colision!")
                exit(0)
        pass
    
        
    def on_event(self, event):
        if event.type == QUIT:
            self.en_juego = False
            
            
    def on_render(self):
        self.display.fill((0, 0, 0))
        self.serpiente.dibujar(self.display, self.imagen)
        self.serpiente.dibujar(self.display, self.imagen_comida)
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
        
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
    juego =  Juego()
    juego.on_execute()