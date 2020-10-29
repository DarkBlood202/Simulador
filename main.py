import os

from configuracion import *
from clases import *
from escenas import *

import pygame


class Simulador(object):
    """
    La clase principal del simulador, maneja las diferentes escenas del simulador, manejo de eventos y etc.
    """
    def __init__(self,ventana):
        self.escenas = [
            Titulo(Fondo(os.path.join(DIR_FONDOS,"title_render.png"),0,0),ventana),
            MenuPrincipal(Fondo(os.path.join(DIR_FONDOS,"main_menu_render.png"),0,0),ventana),
            ComoDisenar(Fondo(os.path.join(DIR_FONDOS,"bubbles_render.png"),0,0),ventana),
            DefinirEmpresa(Fondo(os.path.join(DIR_FONDOS,"area_diseno_0_render.png"),0,0),ventana),
            AreaDiseno(Fondo(os.path.join(DIR_FONDOS,"area_diseno_1_render.png"),0,0),ventana),
            Escena(Fondo(os.path.join(DIR_FONDOS,"area_diseno_2_render.png"),0,0),ventana),
            Escena(Fondo(os.path.join(DIR_FONDOS,"area_diseno_3_render.png"),0,0),ventana),
            Escena(Fondo(os.path.join(DIR_FONDOS,"area_diseno_4_render.png"),0,0),ventana),
            Escena(Fondo(os.path.join(DIR_FONDOS,"area_diseno_5_render.png"),0,0),ventana),
            Escena(Fondo(os.path.join(DIR_FONDOS,"area_diseno_6_render.png"),0,0),ventana),
        ]
        self.contador_escena = 0
        
    def renderizar(self,ventana):
        self.escena_actual.renderizar()

    def actualizar(self):
        # print("Escena: ",self.contador_escena)
        self.escena_actual = self.escenas[self.contador_escena]
        self.escena_actual.actualizar()

    def eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.contador_escena += 1
                    print(self.contador_escena)
                if e.key == pygame.K_LEFT:
                    self.contador_escena -= 1
                    print(self.contador_escena)
                if e.key == pygame.K_UP:
                    print(pygame.mouse.get_pos())

        # Eventos de la escena actual
        self.escena_actual.eventos(eventos)

        # Eventos de los sprites en la escena actual
        for sprite in self.escena_actual.sprites:
            sprite.eventos(eventos)

        # Eventos de la UI en la escena actual
        for element in self.escena_actual.ui:
            element.eventos(eventos)

def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption(TITULO)
    timer = pygame.time.Clock()
    corriendo = True
    fullscreen = False

    simulador = Simulador(ventana)

    while corriendo:
        timer.tick(FPS)

        # Evento de ventana: Si es cerrada
        if pygame.event.get(pygame.QUIT):
            corriendo = False
            return

        # Actualizar instancia simulador
        simulador.actualizar()

        # Eventos de la instancia simulador
        simulador.eventos(pygame.event.get())

        ventana.fill(NEGRO)
        simulador.renderizar(ventana)

        pygame.display.flip()

if __name__ == "__main__":
    main()