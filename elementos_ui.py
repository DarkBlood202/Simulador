import pygame
from configuracion import *
from metodos import *

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

class ListaBarra(pygame.sprite.Sprite):
    def __init__(self,x,y,*elementos):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen(DIR_UI,"lista_barra_0.png")
        self.rect = self.image.get_rect(center=(x,y))

        self.current_time = 0
        self.button_press = 0

        # Lista de las opciones que se mostraran en la lista
        self.elementos = []
        for elemento in elementos:
            self.elementos.append(elemento)

        # Elemento actualmente seleccionado
        self.indice_elemento = 0

        self.anterior = BotonSprite(os.path.join(DIR_UI,"lista_barra_boton_atras"),self.rect.center[0]-67,self.rect.center[1],alts=3)
        self.siguiente = BotonSprite(os.path.join(DIR_UI,"lista_barra_boton_adelante"),self.rect.center[0]+66,self.rect.center[1],alts=3)

        # Texto de la eleccion
        self.texto_renderizar = generar_texto(self.elementos[self.indice_elemento],os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),21,BEIGE_7,fondo=BEIGE_0)
        self.texto_rect = self.texto_renderizar.get_rect(center=(x,y))

    def renderizar(self,ventana):
        # Renderizar fondo de la barra
        ventana.blit(self.image,self.rect)
        # Renderizar botones de navegación de la barra
        ventana.blit(self.anterior.image,self.anterior.rect)
        ventana.blit(self.siguiente.image,self.siguiente.rect)
        # Renderizar texto de la barra
        ventana.blit(self.texto_renderizar,self.texto_rect)

    def actualizar(self):
        self.anterior.actualizar()
        self.siguiente.actualizar()
            
        # Actualizar contador basado en la navegacion con botones
        if self.anterior.encendido:
            if self.indice_elemento == 0:
                self.indice_elemento = len(self.elementos)-1
            else:
                self.indice_elemento -= 1

        if self.siguiente.encendido:
            if self.indice_elemento == len(self.elementos)-1:
                self.indice_elemento = 0
            else:
                self.indice_elemento += 1

        self.texto_renderizar = generar_texto(self.elementos[self.indice_elemento],os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),21,BEIGE_7,fondo=BEIGE_0)
        self.texto_rect = self.texto_renderizar.get_rect(center=(self.rect.center[0],self.rect.center[1]+1))

    def eventos(self,eventos):
        self.anterior.eventos(eventos)
        self.siguiente.eventos(eventos)

class Texto(object):
    def __init__(self,texto,x,y,ruta_fuente,tamano,color,_fondo=None,centro=False):
        self.superficie = generar_texto(texto,ruta_fuente,tamano,color,fondo=_fondo)
        self.cadena_texto = texto
        if centro:
            self.rect = self.superficie.get_rect(center=(x,y))
        else:
            self.rect = self.superficie.get_rect(topleft=(x,y))
    def obtener_texto(self):
        return self.cadena_texto