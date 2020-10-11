import os, pygame

def cargar_imagen(*ruta):
    ruta_imagen = os.path.join(*ruta)
    imagen = pygame.image.load(ruta_imagen)
    return imagen

def generar_texto(texto,ruta_fuente,tamano,color,fondo=None):
    fuente = pygame.font.Font(ruta_fuente,tamano)
    texto_render = fuente.render(texto,True,color,fondo)
    return texto_render

def formatear_millar(numero):
    return "{:,}".format(numero)