```mermaid
classDiagram
    class Cursor{
        -linea int
        -columna int
        -max_posicion tuple
        /posicion:  tuple

        +mover_arriba()
        +mover_abajo()
        +mover_derecha()
        +mover_izquierda()
    }

    class Terminal{
        -_imprimir_secuencia()$
        +limpiar_pantalla()$
        +mover_cursor()$
        +ocultar_cursor()$
    }
```
