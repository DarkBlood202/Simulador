import pygame

class Fondo(pygame.sprite.Sprite):
    """
    La clase Fondo carga un archivo de imagen como Fondo
    """
    def __init__(self,imagen,x,y,centro=False):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load(imagen)
        self.rect = self.imagen.get_rect()
        if centro:
            self.rect.center = (x,y)
        else:
            self.rect.topleft = (x,y)

class Escena(object):
    """
    La clase Escena define lo que se renderiza en la ventana.
    """
    def __init__(self,fondo,ventana):
        self.ventana = ventana
        self.fondo = fondo

    def renderizar(self):
        self.ventana.blit(self.fondo.imagen,self.fondo.rect)

    def actualizar(self):
        pass

    def eventos(self,eventos):
        pass