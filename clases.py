import pygame
from configuracion import *
from metodos import *

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
        self.sprites = pygame.sprite.Group()

    def renderizar(self):
        # Fondo
        self.ventana.blit(self.fondo.imagen,self.fondo.rect)

        # Elementos generales (sprites)
        self.sprites.draw(self.ventana)

        # UI
        self.ui.draw(self.ventana)

    def actualizar(self):
        for element in self.ui:
            element.actualizar()

        for sprite in self.sprites:
            sprite.actualizar()

    def eventos(self,eventos):
        pass

class SpriteGeneral(pygame.sprite.Sprite):
    def __init__(self,sprite,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect(center=(x,y))

    def actualizar(self):
        pass

    def eventos(self,eventos):
        pass
        # CONTROLES PROVISIONALES PARA POSICIONAR ELEMENTOS
        # for e in eventos:
        #     if e.type == pygame.KEYDOWN:
        #         if e.key == pygame.K_w:
        #             self.rect.y -= 1
        #         if e.key == pygame.K_s:
        #             self.rect.y += 1
        #         if e.key == pygame.K_a:
        #             self.rect.x -= 1
        #         if e.key == pygame.K_d:
        #             self.rect.x += 1
        #         print(self.rect.center)

class Contenedor(object):
    def __init__(self,escena):
        self.escena = escena
        self.ui = pygame.sprite.Group()
        self.elementos = []
        self.textos = []

    def renderizar(self,ventana):
        for elemento in self.elementos:
            elemento.renderizar(ventana)

        for texto in self.textos:
            ventana.blit(texto.superficie,texto.rect)

        self.ui.draw(ventana)

    def actualizar(self):
        for ui in self.ui:
            ui.actualizar()

        for elemento in self.elementos:
            elemento.actualizar()

    def eventos(self,eventos):
        for elemento in self.elementos:
            elemento.eventos(eventos)

        for ui in self.ui:
            ui.eventos(eventos)

class Producto(object):
    def __init__(self):
        self.segmento
        self.tamano
        self.tipo_envase
        self.cantidad_colores
        self.porcentaje_calorias
        self.porcentaje_proteinas
        self.sabor
        self.cantidad_produccion
        self.promocion
        self.distribucion