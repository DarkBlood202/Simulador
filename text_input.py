import pygame, sys

class EntradaTexto(object):
    def __init__(self,font,tamano,color,x,y,w,h,x_off=5,y_off=5,background=None,sprite=None):
        self.texto = ""
        self.fuente = pygame.font.Font(font,tamano)
        self.rect = pygame.Rect(x,y,w,h)
        self.activo = False

        self.color = color
        self.x_off = x_off
        self.y_off = y_off
        self.background = background

    def renderizar(self,ventana):
        superficie_texto = self.fuente.render(self.texto,True,self.color,self.background)
        ventana.blit(superficie_texto,(self.rect.x + self.x_off,self.rect.y + self.y_off))

    def obtener_texto(self):
        return self.texto

    def eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(e.pos):
                    self.activo = True
                else:
                    self.activo = False

            if e.type == pygame.KEYDOWN:
                if self.activo:
                    if e.key == pygame.K_BACKSPACE:
                        self.texto = self.texto[:-1]
                    else:
                        self.texto += e.unicode