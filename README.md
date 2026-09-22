# OHM-TUI v1.0 🔋⚡

#### Demo video: https://www.youtube.com
#### Descripción:
OHM-TUI es una calculadora implementada en una interfaz de usuario basada en texto (de sus siglas en inglés TUI: Text User Interface), que permite editar y calcular de manera interactiva las fórmulas referentes a las leyes de Ohm. 

Su arquitectura está implementada directamente sobre la terminal, esto es, que no depende de frameworks como Rich o Textual, sino que consta de una arquitectura MVC dedicada. El objetivo inicial fue implementar una TUI eficiente, lo que conllevó a aprender patrones de diseño y clases desacopladas (diseño modular).

### Patrón MVC
Durante el desarrollo del presente proyecto final, existieron momentos donde agregar una característica adicional superaba límites de complejidad y comprensión concurrente. Es por ello que se investigó acerca de patrones de diseño acordes al objetivo que se trazó en un inicio, crear una interfaz interactiva e intuitiva para el usuario de terminal.

Después de probar con herencia, polimorfismo y un poco de composite, logramos encontrar un patrón que segmentaba las TUIs en algo más que funciones, el patrón MVC:
```mermaid
sequenceDiagram
autonumber
actor usuario as Usuario
participant vista as Vista
participant controlador as Controlador
participant modelo as Modelo

usuario->>vista: Interacción
vista->>controlador: Evento
controlador->>modelo: Modifica datos
modelo-->>controlador: Estado actualizado
controlador->>vista: Renderiza
vista->>usuario: Muestra cambios
```

Siguiendo este principio se logró implementar el proyecto cuyos detalles se abordan a continuación.

### Modelos
Existen dos tipos de modelo en el presente proyecto, el **modelo de dominio** y el **modelo de estado de interfaz**

#### Modelo de dominio (OhmModel)
Se encarga de ejecutar los cálculos y modelamiento de componentes necesarios para obtener el resultado de dominio (por ejemplo, modelar un circuito simple).

##### Ley de Ohm
La ley de Ohm nos dice que al aplicar un potencial eléctrico en los extremos de una resistencia, se producirá una corriente eléctrica a lo largo del circuito.

```txt
                  Resistencia
           *--------/\/\/\/\--------*
           |   ~~~~~> ~~~~~> ~~~~>  |
           |       Corriente        |
Voltaje + ___                       | 
        -  _       Corriente        | 
           |   <~~~~~ <~~~~~ <~~~~  |
           *------------------------*
```

Y que su relación matemática está definida por:

$$
V = I \times R
$$

Cuyas unidades en el sistema internacional son:

$$
V: voltios (V)\\
I: amperios (A)\\
R: ohmios (Ω)
$$

De acuerdo con lo mencionado se muestra un ejemplo de parámetro circuital del sistema:

```mermaid
classDiagram
class Voltaje{
    + unidad: str
    + valor: Decimal
}
class Corriente{
    + unidad: str
    + valor: Decimal
}
class Resistencia{
    + unidad: str
    + valor: Decimal
}
```

Nótese que el atributo valor de cada componente es de tipo Decimal. Esta fue una implementación realizada al final del proyecto, debido a que ofrece una precisión aritmética mucho mayor que el clásico float nativo de python. Cabe resaltar que la librería decimal también es nativa.

```python
suma_normal = 0.1 + 0.1 + 0.1

suma_Decimal = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
```

```text
suma_normal: 0.30000000000000004

suma_Decimal: 0.3
```

#### Cálculo de parámetros. (OhmModel.calcular)
De la fórmula general, se puede deducir el cálculo de los parámetros restantes:

$$
I = \frac{V}{R} \quad \text{y} \quad R = \frac{V}{I}
$$

En las divisiones, hay que tener en cuenta los denominadores, que nunca pueden ser ceros. Por tanto se usan excepciones ***ZeroDivisionError*** e ***InvalidOperation***, esta última excepción es debido al uso de la librería decimal mencionada en el apartado anterior.

Para el caso de calcular corriente:
```python
try:
self.corriente.valor = abs(self.voltaje.valor/self.resistencia.valor)
self.corriente.unidad = 'A'
except (ZeroDivisionError, InvalidOperation):
self.corriente.valor = "ERR"
self.corriente.unidad = ''
```

El valor absoluto se implementa por fines meramente de cálculo escalar.

*_Este proceso lo realiza el método calcular de OhmModel._

#### Notación de Ingeniería (OhmModel.normalizar)
Para representar una magnitud física, existe la **Notación Científica** y la **Notación de Ingeniería**.

Supongamos que queremos representar una corriente de 0.000047 amperios:

Notación Científica:

$$
4.7 \times 10^{-5} A
$$

Notación de Ingeniería:

$$
47 \, \mu\text{A}
$$

Los prefijos SI, en su última actualización (año 2022) incluyó los valores de Quetta y Quecto a su lista oficial. Quedando de la siguiente manera: 

```python
si_exp = {
    -30: 'q', -27: 'r', -24: 'y', -21: 'z', -18: 'a', -15: 'f', -12: 'p', -9: 'n', -6: 'u', -3: 'm',
    0: '',
    3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y', 27: 'R', 30: 'Q'
    }
```

##### Algoritmo de conversión
Para aplicar notación de ingeniería a las magnitudes involucradas en el modelo, se requiere mantener la mantisa en el siguiente rango:

$$
1 \leq \left| mantisa \right| < 1000
$$

Para lograr esto, se implementa un algoritmo directo y fácil de entender. Consiste en multiplicar o dividir iterativamente el número hasta alcanzar una mantisa (valor numérico) en el rango de 1 y 1000
```python
while mantisa < 1:
mantisa *= 1000
exponente -= 3
while mantisa >= 1000:
mantisa /= 1000
exponente += 3
```

Luego se redondea (en el presente proyecto a dos cifras) usando el método quantize de decimal.

```python
mantisa = mantisa.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
```

ROUND_HALF_EVEN es el redondeo estándar utilizado para metrología de precisión según la norma ASTM E29.

Por último se verifica nuevamente si la mantisa subió a 1000.00 (caso especial), además se verifica si el exponente no ha excedido la notación de ingeniería (Quetta y Quecto)

```python
while mantisa >= 1000:
mantisa /= 1000
exponente += 3
```

El exponente resultante es convertido a su símbolo prefijo SI, mediante el diccionario mostrado:
```python
if exponente <= 30 and exponente >=-30:
parametro.prefijo_si = si_exp[exponente]
```

Para al final componerlo de la manera:
$$
magnitud = mantisa [prefijo SI][unidad SI]
$$

*_Este proceso de conversión lo realiza el método OhmModel.normalizar del presente modelo._

#### Modelo Final
Finalmente, integrando cada parte del modelo, se muestra su representación completa.

```mermaid
classDiagram
class OhmModel{
    
    -calcular()

    +normalizar()
}
class Voltaje {
    - unidad: str
    + valor: Decimal
}
OhmModel *-- Voltaje : componente de modelo
class Resistencia {
    - unidad: str
    + valor: Decimal
}
OhmModel *-- Resistencia : componente de modelo
class Corriente {
    - unidad: str
    + valor: Decimal
}
OhmModel *-- Corriente : componente de modelo
```

### Terminal
Terminal es un módulo creado para manejar la impresión de secuencias ANSI usando lenguaje python; como, por ejemplo, la secuencia para limpiar pantalla (un equivalente a clear en linux o cls en windows).

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
Con la finalidad de implementar una arquitectura eficiente, se requirió modularizar el sistema en componentes separados con responsabilidad única. Para el caso de este módulo (cursor) se muestra la representación UML respectiva:

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

#### Menú de Cálculos
Para este tipo de menús se integra el modelo OhmModel implementado en apartados anteriores.
```mermaid
classDiagram
class MenuCalcularVoltaje{
    - cursor: Cursor
    - banner: list[str]
    - opt_str_list: list[str]
    - footer: list[str]
    - navigable: bool
    +render()
}
class OhmModel{
    - resistencia: Resistencia
    - corriente: Corriente
    - voltaje: Voltaje
    + normalizar()
}
MenuCalcularVoltaje *-- OhmModel  : componente dedicado
class Cursor {
    - min_posicion: tuple[int, int]
    - max_posicion: tuple[int, int]
    - posicion: tuple[int, int]
    - symbol: str
    + mover()
}
MenuCalcularVoltaje *-- Cursor : componente dedicado
```

De la misma manera se crearon los siguientes menús: 
- MenuCalcularCorriente
- MenuCalcularResistencia

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

Imaginemos que estamos en el main menu, y el usuario selecciona la opción **1.** (Calcular Voltaje), entonces el menú que debe apilarse sería MenuCalcularVoltaje. Quedando la pila de la siguiente manera.

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

#### Edición de parámetros
En algunos menús, es necesario modificar parámetros, para mantener una interacción cómoda se opta por usar el cursor (por ejemplo █) y dar un salto hacia el punto de edición. De esta manera, con una tecla podemos activar el modo edición.
```text
====================================
     CÁLCULO DE VOLTAJE
====================================
> 1.1. Corriente (I)    : █.0
1.2. Resistencia (R)  : 0.0
-----------------
Resultado (V)         : 0.0
====================================
Editar [l] . Volver [h] . Ayuda [?]
```


## Tests
Para probar exhaustivamente el flujo de funcionamiento de la TUI se hizo uso de pytest.mark.parametrize, la cual es una herramienta que nos permite realizar pruebas iterativas con distintas combinaciones de entradas posibles.

Por ejemplo, para verificar el funcionamiento del cursor implementado. Se prueban distintas combinaciones de movimiento.

```python
data_mover_cursor = [
    (['k'], (1, 1)),
    (['k', 'j'], (2, 1)),
    (['k', 'j', 'j'], (3, 1)),
    (['k', 'j', 'j', 'j'], (4, 1)),
    (['k', 'j', 'j', 'j', 'j'], (5, 1)),
    (['k', 'j', 'j', 'j', 'j', 'j', 'j'], (5, 1)),
    ]
@pytest.mark.parametrize("secuencia_de_movimiento, posicion_cursor", data_mover_cursor)
def test_mover_cursor(secuencia_de_movimiento, posicion_cursor):
posicion_final = mover_cursor(secuencia_de_movimiento)

assert posicion_final == posicion_cursor
```
Este tipo de parametrización no se sería posible sin los wrappers implementados en el archivo principal project.py.

Por ejemplo para los test anteriores se usa el wrapper mover_cursor(), que simula leer una secuencia de teclas ingresadas por un usuario; para finalmente comprobar la posición del cursor (tupla) al terminar dicha secuencia.

```python
def mover_cursor(secuencia_entrada: list[str]) -> tuple[int, int]:
controller = Controller()
 
for tecla_entrada in secuencia_entrada:
    controller.kb_val = tecla_entrada
    controller.exec_kb()
 
return controller.menu_stack[-1].cursor.posicion 
```

De una manera análoga se implementaron en total los siguientes wrappers para testing: 
- mover_cursor()
- navegar()
- calcular_parametro()
- normalizar_parametro()

En general se obtuvieron 75 tests pasados, que prueban cada característica del sistema implementado:

```text
...
test_project.py::test_normalizar_parametro[secuencia_entrada34-corriente-valor34-1.00 kA] PASSED [ 98%]
test_project.py::test_normalizar_parametro[secuencia_entrada35-resistencia-valor35-1.00 k\u03a9] PASSED [100%]

=========================== 75 passed in 0.07s ===========================
```

## Estructura de archivos
- project.py: archivo principal, que maneja al controlador del proyecto implementado.
- README.md: archivo de información del proyecto implementado, detalla cada módulo y su funcionamiento, muestra diagramas UML y código de testing.
- requirements.txt: contiene una sola librería (readchar), la cual es necesaria para leer entradas sin un salto de línea adicional.
- test_project.py: archivo de pruebas, para el cual se utilizó parametrize, lo que permitió implementar el testing secuencias de entrada de una manera iterativa. Además, se utilizaron wrappers de funcionalidad, que imitan el comportamiento de la arquitectura interna, utilizando como objeto principal la clase Controller, el cual es el núcleo del sistema.
