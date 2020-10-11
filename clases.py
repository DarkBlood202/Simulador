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

class BotonUI(pygame.sprite.Sprite):
    def __init__(self,sprite_family,x,y,estado=BOTON_NEUTRAL):
        pygame.sprite.Sprite.__init__(self)
        # Crear lista donde se guardara la familia de sprites para el boton
        self.sprite_family = []
        # Se carga la familia de sprites a la lista
        for i in range(4):
            self.sprite_family.append(cargar_imagen(DIR_UI,str(sprite_family) + "_{}.png".format(i)))
        # Se guarda el estado con el que se inicializo el boton
        self.estado = estado
        # Se establece el sprite que llevará el boton
        self.image = self.sprite_family[self.estado]
        self.rect = self.image.get_rect(center=(x,y))

        # Flag para mantener el estado CLICK
        self.en_click = False

    def actualizar(self):
        # Actualizar el estado del boton
        if self.estado != BOTON_DESACTIVADO and not self.en_click:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.estado = BOTON_ACTIVO
            else:
                self.estado = BOTON_NEUTRAL
        elif self.en_click:
            self.estado = BOTON_CLICK
        
        # Cambiar el sprite de acuerdo al estado del boton
        self.image = self.sprite_family[self.estado]

    def eventos(self,eventos):
        if self.estado != BOTON_DESACTIVADO:
            for e in eventos:
                if e.type == pygame.MOUSEBUTTONDOWN and self.estado == BOTON_ACTIVO:
                    if e.button == MOUSE_IZQUIERDO:
                        self.estado == BOTON_CLICK
                        self.en_click = True
                if e.type == pygame.MOUSEBUTTONUP and self.en_click:
                    if e.button == MOUSE_IZQUIERDO:
                        self.en_click = False

class BotonSprite(pygame.sprite.Sprite):
    def __init__(self,ruta_sprites,x,y,alts=1):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.alts = alts
        for i in range(alts):
            self.sprites.append(cargar_imagen(str(ruta_sprites)+"_{}.png".format(i)))

        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(x,y))

        self.centro_x = self.rect.center[0]
        self.centro_y = self.rect.center[1]

        # Propiedades del botón
        self.encendido = False
        self.desactivado = False

        self.activo = False

    def actualizar(self):
        # Si el mouse esta sobre el boton
        if not self.desactivado and not self.encendido:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.activo = True
            else:
                self.activo = False

        # Cambiar graficos de acuerdo a estado
        if not self.desactivado:
            if self.activo:
                # Se activa el alt si es que existe
                if self.alts > 1:
                    self.image = self.sprites[1]
                else:
                    self.image = self.sprites[0]
            else:
                self.image = self.sprites[0]
        else:
            if self.alts > 3:
                self.image = self.sprites[3]
        if self.encendido and self.alts > 2:
            self.image = self.sprites[2]

        # Actualizar posición del centro:
        self.rect = self.image.get_rect()
        self.rect.center = (self.centro_x,self.centro_y)

    def eventos(self,eventos):
        if not self.desactivado:
            for e in eventos:
                if e.type == pygame.MOUSEBUTTONDOWN and self.activo:
                    if e.button == MOUSE_IZQUIERDO:
                        self.encendido = True
                if e.type == pygame.MOUSEBUTTONUP and self.encendido:
                    if e.button == MOUSE_IZQUIERDO:
                        self.encendido = False

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
        self.elementos = pygame.sprite.Group()

    def renderizar(self):
        self.elementos.draw(self.escena.ventana)

    def actualizar(self):
        for elemento in self.elementos:
            elemento.actualizar()