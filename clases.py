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
        # Listas de elementos dentro de la escena
        self.ui = pygame.sprite.Group()

    def renderizar(self):
        # Fondo
        self.ventana.blit(self.fondo.imagen,self.fondo.rect)

        # Elementos generales (sprites)

        # UI
        self.ui.draw(self.ventana)


    def actualizar(self):
        pass

    def eventos(self,eventos):
        pass

class Boton(pygame.sprite.Sprite):
    def __init__(self,sprite,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect(center=(x,y))