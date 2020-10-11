from configuracion import *
from clases import Escena, Boton, SpriteGeneral, BotonUI, BotonSprite, Contenedor
from text_input import EntradaTexto
from metodos import *

import pygame

class Titulo(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando objetos nuevos en la escena
        boton_tarjetero = Boton(cargar_imagen(DIR_ELEMENTOS,"titulo","tarjetero.png"),479,281).add(self.ui)

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
        boton_chart = BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","chart"),688,307,alts=2).add(self.ui)
        boton_monitor = BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","monitor"),186,262,alts=2).add(self.ui)
        boton_papelera = BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","papelera"),688,513,alts=2).add(self.ui)
        # boton_globo = Boton(cargar_imagen(DIR_ELEMENTOS,"globo.png"),513,274).add(self.ui)
        # boton_cafe = Boton(cargar_imagen(DIR_ELEMENTOS,"cafe.png"),59,336).add(self.ui)

        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_1"),608,76,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_2"),628,84,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_3"),653,69,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_4"),679,80,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_5"),698,76,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_6"),721,84,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_7"),740,70,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_8"),757,75,alts=2).add(self.ui)

        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_9"),610,180,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_10"),631,172,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_11"),652,172,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_12"),670,171,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_13"),687,180,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_14"),703,166,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_15"),722,177,alts=2).add(self.ui)
        BotonSprite(os.path.join(DIR_ELEMENTOS,"menu_principal","books","book_16"),747,165,alts=2).add(self.ui)


class ComoDisenar(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando nuevos objetos en la escena
        burbuja_grande = SpriteGeneral(cargar_imagen(DIR_ELEMENTOS,"pensamiento","bubble_big.png"),619,97).add(self.sprites)
        # burbuja_media = SpriteGeneral(cargar_imagen(DIR_ELEMENTOS,"bubble_med.png"),450,221).add(self.sprites)
        # burbuja_pequena = SpriteGeneral(cargar_imagen(DIR_ELEMENTOS,"bubble_small.png"),356,276).add(self.sprites)

class DefinirEmpresa(Escena):
    def __init__(self,fondo,ventana):
        # Cargando el constructor de la clase Padre
        super().__init__(fondo,ventana)

        # Instanciando nuevos objetos en la escena
        self.entrada_texto = EntradaTexto(os.path.join(DIR_ASSETS,"fonts","Vidaloka-Regular.ttf"),24,BEIGE_8,264,96,400,30,x_off=5,y_off=0,background=BEIGE_0)

        # Botones de seleccion de logo
        logos = []

        logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoA"),168,204,alts=3))
        logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoB"),317,204,alts=3))
        logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoC"),465,204,alts=3))
        logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoD"),613,204,alts=3))

        for logo in logos:
            logo.add(self.ui)

        # Boton de confirmar
        self.boton_confirmar = BotonUI("boton_confirmar",391,307)
        self.boton_confirmar.estado = BOTON_DESACTIVADO
        self.boton_confirmar.add(self.ui)

        # Variables
        self.nombre_empresa = self.entrada_texto.obtener_texto()

    def actualizar(self):
        super().actualizar()
        
        # Logica de la escena:
        # Activar/Desactivar botón de confirmar
        if self.entrada_texto.obtener_texto() != "":
            self.boton_confirmar.estado = BOTON_NEUTRAL
        else:
            self.boton_confirmar.estado = BOTON_DESACTIVADO

    def renderizar(self):
        # Renderizando los elementos por defecto de la escena
        super().renderizar()
        # Renderizar caja de texto
        self.entrada_texto.renderizar(self.ventana)

    def eventos(self,eventos):
        self.entrada_texto.eventos(eventos)
        

class AreaDiseno(Escena):
    def __init__(self,fondo,ventana):
        super().__init__(fondo,ventana)

        self.presupuesto = 45000000
        self.periodo = 1
        self.producto = 1

        # Generar texto para los numeros
        self.texto_periodo = generar_texto("N° " + str(self.periodo).zfill(2),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),17,BEIGE_0,fondo=BEIGE_1)
        self.texto_producto = generar_texto("N° " + str(self.producto).zfill(3),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),17,BEIGE_0,fondo=BEIGE_1)
        self.texto_presupuesto = generar_texto(formatear_millar(self.presupuesto),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),16,BEIGE_0,fondo=BEIGE_1)

        # Modulos de Estudio - Diseño de Producto - Producción - Promoción - Distribución
        self.modulo_estudio = Contenedor(self)
        self.modulo_diseno = Contenedor(self)
        self.modulo_produccion = Contenedor(self)
        self.modulo_promocion = Contenedor(self)
        self.modulo_distribucion = Contenedor(self)

        # AGregar elementos correspondientes a cada modulo


    def renderizar(self):
        super().renderizar()
        self.ventana.blit(self.texto_periodo,pygame.Rect(195,106,145,24))
        self.ventana.blit(self.texto_producto,pygame.Rect(368,106,145,24))
        self.ventana.blit(self.texto_presupuesto,pygame.Rect(547,106,145,24))

    def actualizar(self):
        super().actualizar()
        self.texto_periodo = generar_texto("N° " + str(self.periodo).zfill(2),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),17,BEIGE_0,fondo=BEIGE_1)
        self.texto_producto = generar_texto("N° " + str(self.producto).zfill(3),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),17,BEIGE_0,fondo=BEIGE_1)
        self.texto_presupuesto = generar_texto(formatear_millar(self.presupuesto),os.path.join(DIR_FONTS,"Vidaloka-Regular.ttf"),16,BEIGE_0,fondo=BEIGE_1)
