# OHM-TUI v1.0 🔋⚡

#### Demo video: https://www.youtube.com
#### Descripción:
OHM-TUI es una calculadora implementada en una interfaz de usuario basada en texto (de sus siglas en inglés TUI: Text User Interface), que permite editar y calcular de manera interactiva las fórmulas referentes a las leyes de Ohm. 

Su arquitectura está implementada a nivel de interprete, esto es, que no depende de frameworks como Rich o Textual, sino que consta de una arquitectura MVC dedicada, con la finalidad de ir más allá del rendimiento; como, por ejemplo, el aprendizaje de patrones de software y clases desacopladas (diseño modular).

## MODULOS IMPLEMENTADOS

### Terminal
Terminal es un módulo creado para manejar la impresion de secuencias ANSI usando lenguaje python; como, por ejemplo, la secuencia para limpiar pantalla (un equivalente a clear en linux o cls en windows).

**Secuencias implementadas:**

- Limpiar pantalla: "\33[2J"
- Mover cursor (línea, columna): f"\033[{line};{column}f"
- Ocultar Cursor: "\033[?25l"
- Mostrar Cursor: "\033[?25h"

**Combinación de secuencias:**

- Limpiar pantalla + Mover Cursor


### Cursor (selector de opción)
El cursor representa al típico puntero de opción en los menús que indica cual opción es la seleccionada.
Su icono puede ser un símbolo representativo que le indique al usuario en que opción está, ejemplos típicos son **>**, **>>** o **▶**. Para el presente proyecto se opta por el símbolo **>** con una motivación meramente estética.

#### Representación del cursor implementado.
Debido a la necesidad de implementar un proyecto de esta magnitud, se requirió modularizar cada componente de tal modo que sean independientes unos de otros. Para el caso de este módulo su representación UML es la siguiente:

```mermaid
classDiagram
    class Cursor{
        - símbolo: str
        - max_posicion:  tuple[int, int]
        - min_posicion:  tuple[int, int]
        - linea: int
        - columna: int

        +mover_arriba()
        +mover_abajo()
        +mover_derecha()
        +mover_izquierda()

        +posicion()
        +rel_posicionY()
    }
```


### Menus
Una TUI siempre muestra al usuario una capa de visualización, que le permite al mismo manejarse entre las diversas opciones implementadas en dicha TUI. Por ejemplo el menú principal, que suele contener las opciones principales del sistema.

```bash
===========================================
               OHM-TUI v1.0
===========================================
> 1. Calcular Voltaje (V = I × R)
  2. Calcular Corriente (I = V / R)
  3. Calcular Resistencia (R = V / I)
  4. Info
  5. Ayuda
===========================================
subir/bajar [k/j] . Entrar [l] . Salir [q]
```

El menú mostrado, como ejemplo, consta de tres partes claramente segmentadas.
- Cabecera o banner
- Lista de opciones
- Pie o footer

Y aquí también podemos agregar un objeto que ya habíamos creado, el cursor de selección.

Es por ello que se decidió diseñar el objeto MainMenu de la siguiente manera:
```mermaid
classDiagram
    class MainMenu{
        - banner: list[str]
        - opt_str_list: list[str]
        - footer: list[str]
        - navigable: bool
        +render()
    }
    class Cursor {
        - min_posicion: tuple[int, int]
        - max_posicion: tuple[int, int]
        - posicion: tuple[int, int]
        - symbol: str
        + mover()
    }
    MainMenu *-- Cursor : componente dedicado
```
Este diseño desacopla el estado del menú del cursor, generando una arquitectura más limpia y funcional.

De la misma manera se crearon los siguientes menús: 
- MenuAyuda
- MenuInfo
- MenuCalcularVoltaje
- MenuCalcularCorriente
- MenuCalcularResistencia

Más adelante veremos cómo algunos menús están compuestos de otras instancias asociadas (como por ejemplo los menús de cálculo, que necesitan un modelo para renderizar parametros numéricos)


### Controlador
Para generar una interacción entre los componentes mencionados, se decidió crear una clase Controller, cuyo objetivo es el de orquestar el flujo desacoplado y eficiente de cada componente involucrado.

##### Modelo secuencial de interacción 
```mermaid
sequenceDiagram
    autonumber
    actor user as user
    participant controller as Controller
    participant dispatcher as dispatcher
    
    controller->>user: solicita tecla
    user->>controller: ingresa tecla

    controller->>dispatcher: solicita evaluación
    alt si tecla es válida
        dispatcher->>controller: valida ejecución
    end
```

Las acciones implementadas para el presente proyecto son las siguientes:
- Mover cursor abajo
- Mover cursor arriba
- Apilar nuevo menú
- Desapilar último menú
- Salir del programa
- Ir al menú de ayuda

#### Mover cursor
Como se mencionó en el apartado de cursor, este cuenta con métodos que permiten modificar su tupla de posición, donde el primer elemento representa la línea (Y) y el segundo elemento la columna (X).

#### Pila de menús
De nada serviría implementar varios menús, si no tenemos una manera de ordenarlos acorde a lo que el usuario requiera. Es por ello que se opta usar pilas tipo LIFO (Last In First Out), donde cada menu es un elemento de la pila. 

Imaginemos que estamos en el main menu, y el usuario selecciona la opción **1.0** (Calcular Voltaje), entonces el menú que debe apilarse sería MenuCalcularVoltaje. Quedando la pila de la siguiente manera.

```text
  Pila: menu_stack[MainMenu(), MenuCalcularVoltaje(), ...]
        +-------------------------+
        |           ...           | -> render()
        +-------------------------+
        |   MenuCalcularVoltaje   | -> render()
        +-------------------------+
        |        MainMenu         | -> render()
        +-------------------------+
```

El controlador por defecto siempre inicializa con un MainMenu() en su pila (una lista de menús) y el proceso de apilar y desapilar corresponde a métodos append y pop nativos de python para manipular listas.

### Modelo
El modelo, aislado totalmente de los otro módulos, se encarga de ejecutar los cálculos y modelamiento de componentes necesarios para obtener resultados de negocio.

En este caso, para el proyecto se decide utilizar un modelo sencillo, que nos permita eliminar toda complejidad mientras se refactorizan el proyecto. Claro está que una vez maduro el proyecto, el modelo puede ser reemplazado por otro, como un calculador de circuitos RC.


