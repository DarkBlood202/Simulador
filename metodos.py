import os, pygame

def cargar_imagen(*ruta):
    ruta_imagen = os.path.join(*ruta)
    imagen = pygame.image.load(ruta_imagen)
    return imagen

def dibujar_contorno(imagen,color=(255,255,255),opacidad_minima=127):
    mascara = pygame.mask.from_surface(imagen,opacidad_minima)
    contorno = pygame.Surface(imagen.get_size()).convert_alpha()
    contorno.fill((0,0,0,0))
    for punto in mascara.outline():
        contorno.set_at(punto,color)
    return contorno