from configuracion import *
from clases import Escena, Boton, SpriteGeneral
from metodos import *

from pygame_textinput import TextInput

import pygame

class Titulo(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando objetos nuevos en la escena
        boton_tarjetero = Boton(cargar_imagen(DIR_FONDOS,"elements","tarjetero.png"),479,281).add(self.ui)

    def eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    print("Bienvenido")
                elif e.key == pygame.K_ESCAPE:
                    print("Menu abierto")


class MenuPrincipal(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando objetos nuevos en la escena
        boton_chart = Boton(cargar_imagen(DIR_FONDOS,"elements","chart.png"),688,307).add(self.ui)
        boton_monitor = Boton(cargar_imagen(DIR_FONDOS,"elements","monitor.png"),186,262).add(self.ui)
        boton_globo = Boton(cargar_imagen(DIR_FONDOS,"elements","globo.png"),513,274).add(self.ui)
        boton_cafe = Boton(cargar_imagen(DIR_FONDOS,"elements","cafe.png"),59,336).add(self.ui)
        boton_papelera = Boton(cargar_imagen(DIR_FONDOS,"elements","papelera.png"),688,513).add(self.ui)

class ComoDisenar(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando nuevos objetos en la escena
        burbuja_grande = SpriteGeneral(cargar_imagen(DIR_FONDOS,"elements","bubble_big.png"),619,97).add(self.sprites)
        burbuja_media = SpriteGeneral(cargar_imagen(DIR_FONDOS,"elements","bubble_med.png"),450,221).add(self.sprites)
        burbuja_pequena = SpriteGeneral(cargar_imagen(DIR_FONDOS,"elements","bubble_small.png"),356,276).add(self.sprites)

class AreaDiseno(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando nuevos objetos en la escena
        # self.input_nombre_empresa = TextInput(max_string_length=20)
        # self.caja_texto_nombre_empresa = pygame.Surface((400,30))

        # Botones de seleccion de logo
        boton_logo_0 = Boton(cargar_imagen(DIR_FONDOS,"elements","logos","logo_0.png"),168,204,mantener=True).add(self.ui)
        boton_logo_1 = Boton(cargar_imagen(DIR_FONDOS,"elements","logos","logo_1.png"),317,204,mantener=True).add(self.ui)
        boton_logo_2 = Boton(cargar_imagen(DIR_FONDOS,"elements","logos","logo_2.png"),465,204,mantener=True).add(self.ui)
        boton_logo_3 = Boton(cargar_imagen(DIR_FONDOS,"elements","logos","logo_3.png"),613,204,mantener=True).add(self.ui)

        # Boton de confirmar
        boton_confirmar = Boton(cargar_imagen(DIR_UI,"confirmar.png"),391,307,desactivado=True).add(self.ui)

    def renderizar(self):
        # Renderizando los elementos por defecto de la escena
        super().renderizar()
        # Renderizar caja de texto
        # self.caja_texto_nombre_empresa.fill(pygame.Color("#f9f9f9"))
        # self.caja_texto_nombre_empresa.blit(self.input_nombre_empresa.get_surface(),(5,3))
        # self.ventana.blit(self.caja_texto_nombre_empresa,(264,96))

    # def eventos(self,eventos):
    #     self.input_nombre_empresa.update(eventos)

