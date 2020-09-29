from configuracion import *
from clases import Escena, Boton
from metodos import *

import pygame

class Titulo(Escena):
    def __init__(self,fondo,ventana):
        super().__init__(fondo,ventana)
        img = cargar_imagen(DIR_UI,"test.png")
        botonPruebas = Boton(img,400,300)
        botonPruebas.add(self.ui)

    def actualizar(self):
        pass

    def eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    print("You've pressed SPACE")

