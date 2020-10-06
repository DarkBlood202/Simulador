from configuracion import *
from clases import Escena, Boton
from metodos import *

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

class ComoDisenar(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando nuevos objetos en la escena