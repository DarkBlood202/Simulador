# REPORTE DE COMMIT
[10/10/2020]
---
---
## HECHO
---
+ #### Diseño de los modulos del Área de Diseño
    + Se diseñó la estructura de la interfaz de usuario para implementar al simulador.
+ #### Implementación inicial de una clase Contenedor
    + Para agrupar elementos en módulos dentro de una misma escena.
---
## TODO LIST
---
+ #### Funcionalidad de los módulos
    + Conectar la interfaz de usuario con la lógica del programa.
    + Entrada y salida de datos de los módulos.
+ #### Cambio de escena por eventos de botones de la GUI
    + Cambiar de escena manejado por acciones de botones en la interfaz de usuario.
---
[09/10/2020]
---
---
## HECHO
---
+ #### Reconstrucción de una clase Entrada de Texto:
    + Se eliminó el error del cambio de escena.

[08/10/2020]
---
---
## HECHO
---
+ #### Reconstruir la clase Botón:
    + Se establece un estándar de nomenclatura para el archivo de sprites:

        > Ejemplo:  
    boton_confirmar_0.png [NEUTRAL]  
    boton_confirmar_1.png [HOVER]  
    boton_confirmar_2.png [ON CLICK]  
    boton_confirmar_3.png [DISABLED]

    + Los archivos se cargan a una lista cuyos indices se corresponden con el sufijo numérico del archivo que a su vez corresponden al estado del botón.
---
[06/OCT/2020]
---
---
## TODO LIST
---
+ #### Reconstruir la clase Botón:
    + Debe implementar los 4 estados de un botón:
        + Neutral
        + En área activa (_hover_)
        + Activado (_onClick_)
        + Deshabilitado (_disabled_)
    + Debe tener un gráfico para cada estado.
+ #### Implementar una clase GrupoBotones.
    + Los botones contenidos en ella deben poder interactuar unos con otros.
    + Los botones contenidos en ella deben "saber" que existen los otros.


---
## BUGS Y ERRORES
---
+ TextInput regresa a la escena anterior por alguna razón inexplicable.