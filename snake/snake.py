import pygame, sys
from pygame.locals import *

class Serpiente:
    posicion_en_x = 10
    posicion_en_y = 10
    velocidad = 1
    
    def mover_izquierda(self):
        self.posicion_en_x = self.posicion_en_x - self.velocidad

    def mover_derecha(self):
        self.posicion_en_x = self.posicion_en_x + self.velocidad
        
    def mover_arriba(self):
        self.posicion_en_y = self.posicion_en_y - self.velocidad
        
    def mover_abajo(self):
        self.posicion_en_y = self.posicion_en_y + self.velocidad




    

class Juego:
    largo_ventana = 800
    ancho_ventana = 600
    serpiente = None
    en_juego = None
    display = None
    imagen = None
    nombre_imagen = "serpiente.png"
    def __init__(self):
        self.en_juego = True
        self.serpiente = Serpiente()
        
    def on_init(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.ancho_ventana, self.largo_ventana), pygame.HWSURFACE)
        
        pygame.display.set_caption('Mi juiguito de snake')
        self.en_juego = True
        self.imagen = pygame.image.load(self.nombre_imagen).convert()
        
        
    def espera(self):
        pass
    
    def on_event(self, event):
        if event.type == QUIT:
            self.en_juego = False
            
    def on_render(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.imagen, (self.serpiente.posicion_en_x, self.serpiente.posicion_en_y))
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
                
            self.espera()
            self.on_render()
        
        self.on_cleanup()
    
    
if __name__ == "__main__":
    juego =  Juego()
    juego.on_execute()