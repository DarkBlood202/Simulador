from clases import Escena

import pygame

class Titulo(Escena):
    def actualizar(self):
        pass

    def eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    print("You've pressed SPACE")