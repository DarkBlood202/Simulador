import os

ANCHO = 800
ALTO = 600

TITULO = "Simulador de Marketing"

FPS = 60

# Directorios
DIR_BASE = os.path.dirname(__file__)
DIR_ASSETS = os.path.join(DIR_BASE,"data")
DIR_FONDOS = os.path.join(DIR_ASSETS,"bck")
DIR_UI = os.path.join(DIR_ASSETS,"ui")

# Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)

# Constantes
MOUSE_IZQUIERDO = 1
MOUSE_DERECHO = 3