# Diagramas UML

## Diagramas de Clase

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
## Diagramas de secuencia:

```mermaid
sequenceDiagram
   Bernard->>+kitty: python project.py
   kitty->>+MenuView0: getview()
   MenuView0->>+Cursor: set_CursorLimits(Ymax, Xmax)
   MenuView0->>+Cursor: getCursorPos()
   Cursor-->>-MenuView0: SendCursorPos"(Y=0, X=0)"
   MenuView0-->>-Bernard: MenuList[0]
   
   rect rgb(240, 248, 255)
   opt Si presiona 'j'
      Bernard->>+InputHandler: presionar 'j'
      InputHandler-->>Bernard: print("presionaste j!")
      alt Si CursorY < LímiteYmax
         InputHandler->>Cursor: setCursorYPos("+1")
      else Límite superado
         InputHandler-->>Bernard: print("límite Ymax superado")
      end
      deactivate InputHandler
   end
   end

   rect rgb(255, 240, 245)
   opt Si presiona 'k'
      Bernard->>+InputHandler: presionar 'k'
      InputHandler-->>Bernard: print("presionaste k!")
      alt Si CursorY > LímiteYmin
         InputHandler->>Cursor: setCursorYPos("-1")
      else LímiteY mínimo superado
         InputHandler-->>Bernard: print("límite Ymin superado")
      end
      deactivate InputHandler
   end
   end
```

j
