import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("Titulo")
    screen = pygame.display.set_mode((480,360))

    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()

if __name__ == '__main__':
    main()