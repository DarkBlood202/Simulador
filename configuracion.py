import os
from pygame import Color

ANCHO = 800
ALTO = 600

TITULO = "Simulador de Marketing"

FPS = 60

# Directorios #
DIR_BASE = os.path.dirname(__file__)
DIR_ASSETS = os.path.join(DIR_BASE,"data")
DIR_FONDOS = os.path.join(DIR_ASSETS,"bck")
DIR_ELEMENTOS = os.path.join(DIR_FONDOS,"elements")
DIR_UI = os.path.join(DIR_ASSETS,"ui")
DIR_FONTS = os.path.join(DIR_ASSETS,"fonts")

# Colores #
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)

# Paleta de colores del Simulador
BEIGE_0 = Color("#f4e3d7")
BEIGE_1 = Color("#e9c6af")
BEIGE_2 = Color("#deaa87")
BEIGE_3 = Color("#d38d5f")
BEIGE_4 = Color("#c87137")
BEIGE_5 = Color("#a05a2c")
BEIGE_6 = Color("#784421")
BEIGE_7 = Color("#502d16")
BEIGE_8 = Color("#28170b")

# Constantes #
# Mouse
MOUSE_IZQUIERDO = 1
MOUSE_DERECHO = 3

# Botones
BOTON_NEUTRAL = 0
BOTON_ACTIVO = 1
BOTON_CLICK = 2
BOTON_DESACTIVADO = 3