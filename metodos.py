import os, pygame

def cargar_imagen(*ruta):
    ruta_imagen = os.path.join(*ruta)
    imagen = pygame.image.load(ruta_imagen)
    return imagen