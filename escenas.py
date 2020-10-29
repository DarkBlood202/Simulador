from configuracion import *
from clases import Escena, SpriteGeneral, Contenedor
from elementos_ui import *
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
        self.entrada_texto = EntradaTexto(VIDALOKA,24,BEIGE_8,264,96,400,30,x_off=5,y_off=0,background=BEIGE_0)

        # Botones de seleccion de logo
        self.logos = []

        self.logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoA"),168,204,alts=3))
        self.logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoB"),317,204,alts=3))
        self.logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoC"),465,204,alts=3))
        self.logos.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"definir_empresa","logos","logoD"),613,204,alts=3))

        for logo in self.logos:
            logo.add(self.ui)

        # Boton de confirmar
        self.boton_confirmar = BotonUI("boton_confirmar",391,307)
        self.boton_confirmar.estado = BOTON_DESACTIVADO
        self.boton_confirmar.add(self.ui)

        # Variables
        self.nombre_empresa = self.entrada_texto.obtener_texto()
        self.logo_empresa = 0

    def actualizar(self):
        super().actualizar()
        
        ##################### LOGICA DE LA ESCENA #####################

        # Botones de selección de logo
        for indice,logo in enumerate(self.logos):
            if logo.encendido:
                self.logo_empresa = indice

        # Activar/Desactivar botón de confirmar
        if self.boton_confirmar.estado != BOTON_CLICK:
            if self.entrada_texto.obtener_texto() == "":
                self.boton_confirmar.estado = BOTON_DESACTIVADO
            elif not self.boton_confirmar.estado == BOTON_ACTIVO:
                self.boton_confirmar.estado = BOTON_NEUTRAL

        # Si confirmas la selección
        if self.boton_confirmar.estado == BOTON_CLICK:
            self.nombre_empresa = self.entrada_texto.obtener_texto()
            print(self.nombre_empresa)
            print(f"Logo: {self.logo_empresa}")

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

        self.modulos = []
        for i in range(5):
            self.modulos.append(Contenedor(self))

        self.contador_modulo = 4

        self.modulo_actual = self.modulos[self.contador_modulo]

        self.presupuesto = 45000000
        self.periodo = 1
        self.producto = 1

        # Botones de navegación de módulos
        self.navegacion_anterior = BotonSprite(os.path.join(DIR_UI,"boton_navegacionA"),134,429,alts=3)
        self.navegacion_siguiente = BotonSprite(os.path.join(DIR_UI,"boton_navegacionB"),649,429,alts=3)

        self.navegacion_anterior.add(self.ui)
        self.navegacion_siguiente.add(self.ui)

        # Generar texto para los numeros en la barra superior
        self.texto_periodo = generar_texto("N° " + str(self.periodo).zfill(2),VIDALOKA,17,BEIGE_0,fondo=BEIGE_1)
        self.texto_producto = generar_texto("N° " + str(self.producto).zfill(3),VIDALOKA,17,BEIGE_0,fondo=BEIGE_1)
        self.texto_presupuesto = generar_texto(formatear_millar(self.presupuesto),VIDALOKA,16,BEIGE_0,fondo=BEIGE_1)

        # Agregar elementos correspondientes a cada modulo
        
        ############# MODULO ESTUDIO MERCADO #############
        
        ##################################################

        ############# MODULO DISENO PRODUCTO #############
        self.modulos[1].textos.append(Texto("Tamaño del producto",191,157,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        self.modulos[1].textos.append(Texto("Tipo de envase",191,197,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        self.modulos[1].textos.append(Texto("Colores por empaque",191,237,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        self.modulos[1].textos.append(Texto("Porcentaje de calorías",191,277,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        self.modulos[1].textos.append(Texto("Porcentaje de proteínas",191,317,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        self.modulos[1].textos.append(Texto("Sabor",191,357,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))

        self.modulos[1].elementos.append(ListaBarra(535,169,"0.2L","0.3L","1.0L","4.0L"))
        self.modulos[1].elementos.append(ListaBarra(535,209,"Cartón","Vidrio","Plástico"))
        self.modulos[1].elementos.append(ListaBarra(535,249,"2","3","5"))
        self.modulos[1].elementos.append(ListaBarra(535,289,"18%","26%","35%"))
        self.modulos[1].elementos.append(ListaBarra(535,329,"7%","9%","12%"))
        self.modulos[1].elementos.append(ListaBarra(535,369,"Fresa","Durazno","Piña","Lúcuma","Cereza"))
        self.confirmar_1 = BotonUI("boton_confirmar",391,411)
        self.confirmar_1.estado = BOTON_DESACTIVADO
        self.confirmar_1.add(self.modulos[1].ui)
        ##################################################

        ################ MODULO PRODUCCION ###############
        self.modulos[2].textos.append(Texto("Indique cuánto va a producirse.",244,180,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        
        self.cantidad_produccion = 0
        self.entrada_cantidad_produccion = EntradaTexto(VIDALOKA,24,BEIGE_8,244,211,295,30,x_off=0,y_off=0,background=BEIGE_2)
        self.modulos[2].elementos.append(self.entrada_cantidad_produccion)
        
        self.confirmar_2 = BotonUI("boton_confirmar",391,285)
        self.confirmar_2.estado = BOTON_DESACTIVADO
        self.confirmar_2.add(self.modulos[2].ui)
        ##################################################

        ################ MODULO PROMOCION ################

        ##################################################

        ############### MODULO DISTRIBUCION ##############
        self.modulos[4].textos.append(Texto("Seleccione los canales de distribución.",212,180,VIDALOKA,21,BEIGE_7,_fondo=BEIGE_1))
        
        canales_distribucion = []
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","supermercados"),175,266,alts=4))
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","mercado_abastos"),261,266,alts=4))
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","autoservicios"),347,266,alts=4))
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","bodegas"),433,266,alts=4))
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","panaderias"),519,266,alts=4))
        canales_distribucion.append(BotonSprite(os.path.join(DIR_ELEMENTOS,"area_diseno","distribucion_precio","entrega_domicilio"),605,266,alts=4))

        for canal in canales_distribucion:
            canal.add(self.modulos[4].ui)

        self.boton_confirmar_4 = BotonUI("boton_confirmar",391,385)
        self.boton_confirmar_4.estado = BOTON_DESACTIVADO
        self.boton_confirmar_4.add(self.modulos[4].ui)
        ##################################################

    def renderizar(self):
        # Renderizar elementos de la escena
        super().renderizar()
        # Renderizar texto de la barra superior
        self.ventana.blit(self.texto_periodo,pygame.Rect(195,106,145,24))
        self.ventana.blit(self.texto_producto,pygame.Rect(368,106,145,24))
        self.ventana.blit(self.texto_presupuesto,pygame.Rect(547,106,145,24))

        # Renderizar modulo
        self.modulo_actual.renderizar(self.ventana)

    def actualizar(self):
        super().actualizar()
        self.texto_periodo = generar_texto("N° " + str(self.periodo).zfill(2),VIDALOKA,17,BEIGE_0,fondo=BEIGE_1)
        self.texto_producto = generar_texto("N° " + str(self.producto).zfill(3),VIDALOKA,17,BEIGE_0,fondo=BEIGE_1)
        self.texto_presupuesto = generar_texto(formatear_millar(self.presupuesto),VIDALOKA,16,BEIGE_0,fondo=BEIGE_1)

        # Actualizar contador basado en navegación con botones
        if self.navegacion_anterior.encendido:
            print(f"Modulo: {self.contador_modulo}")
            if self.contador_modulo == 0:
                self.contador_modulo = 0
            else:
                self.contador_modulo -= 1

        if self.navegacion_siguiente.encendido:
            print(f"Modulo: {self.contador_modulo}")
            if self.contador_modulo == len(self.modulos)-1:
                self.contador_modulo = len(self.modulos)-1
            else:
                self.contador_modulo += 1

        # Actualizar modulo actual
        self.modulo_actual = self.modulos[self.contador_modulo]
        self.modulo_actual.actualizar()

        # Lógica modulo-especifica
        
        ################ MODULO PRODUCCION ###############
        # Activar/Desactivar botón de confirmar
        if self.confirmar_2.estado != BOTON_CLICK:
            if self.entrada_cantidad_produccion.obtener_texto() == "":
                self.confirmar_2.estado = BOTON_DESACTIVADO
            elif not self.confirmar_2.estado == BOTON_ACTIVO:
                self.confirmar_2.estado = BOTON_NEUTRAL

        # Si confirmas la selección
        if self.confirmar_2.estado == BOTON_CLICK:
            # Debes haber introducido un numero
            try:
                self.cantidad_produccion = int(self.entrada_cantidad_produccion.obtener_texto())
            except ValueError:
                print("Introduce un número.")
            finally:
                print(self.cantidad_produccion)
        ##################################################

    def eventos(self,eventos):
        self.modulo_actual.eventos(eventos)