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

class Boton(pygame.sprite.Sprite):
    def __init__(self,sprite,x,y,mantener=False,desactivado=False):
        pygame.sprite.Sprite.__init__(self)
        # Se inicializa la imagen vacia
        self.imagen_vacia = pygame.Surface(sprite.get_size(),pygame.SRCALPHA,32)
        # Se inicializa la imagen activa
        self.imagen_activa = sprite

        # Se establece imagen vacia como imagen de objeto
        self.image = self.imagen_vacia
        self.rect = self.image.get_rect(center=(x,y))
        
        # Si el boton tiene la propiedad de "permanecer" activado
        self.mantener = mantener
        
        # Si el boton esta desactivado al momento de crearse
        self.desactivado = desactivado

        self.area_activa = False
        self.ya_activado = False

    def actualizar(self):
        if not self.desactivado:
            # Detección del cursor en colision con el botón
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.area_activa = True
            else:
                self.area_activa = False

            # Cuando el boton se encuentra en su area activa
            if self.area_activa:
                self.image = self.imagen_activa
            else:
                if not self.ya_activado:
                    self.image = self.imagen_vacia

    def accion(self):
        pass

    def eventos(self,eventos):
        if not self.desactivado:
            for e in eventos:
                if e.type == pygame.MOUSEBUTTONDOWN and self.area_activa:
                    if e.button == MOUSE_IZQUIERDO:
                        if self.mantener:
                            self.ya_activado = True
                        self.accion()

            # CONTROLES PROVISIONALES PARA MOVER LOS BOTONES
            # if e.type == pygame.KEYDOWN:
            #     if e.key == pygame.K_w:
            #         self.rect.y -= 1
            #     if e.key == pygame.K_s:
            #         self.rect.y += 1
            #     if e.key == pygame.K_a:
            #         self.rect.x -= 1
            #     if e.key == pygame.K_d:
            #         self.rect.x += 1
            #     print(self.rect.center)

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

