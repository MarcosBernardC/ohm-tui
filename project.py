from readchar import readkey
import sys
from dataclasses import dataclass, field
from modules.terminal import Terminal


@dataclass
class Cursor:
    symbol: str = '>'
    max_posicion: tuple[int, int] = (10, 1)
    min_posicion: tuple[int, int] = (1, 1)
    opt: int = 0
    linea: int = 1
    columna: int = 1

    def mover_arriba(self):
        if self.linea > self.min_posicion[0]:
            self.linea -= 1
            self.opt -= 1
    
    def mover_abajo(self):
        if self.linea < self.max_posicion[0]:
            self.linea += 1
            self.opt += 1

    def mover_derecha(self):
        if self.columna < self.max_posicion[1]:
            self.columna += 1

    def mover_izquierda(self):
        if self.columna > self.min_posicion[1]:
            self.columna -= 1

    @property
    def posicion(self):
        return (self.linea, self.columna)

    @posicion.setter
    def posicion(self, value: tuple[int, int]):
        self.linea = value[0]
        self.columna = value[0]

@dataclass
class MenuView0: #main menu
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[15*'-', "Main Menu", 15*'-'])
    opt_str_list: list=field(default_factory=lambda:["Calcular Voltaje (V = I * R)", "Ayuda"])

    def render(self):
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(f"  {str_opt}")

        print('\n'.join(menu_str))

    def handle_input(self, value):
        match value:
            case 'j': self.cursor.mover_abajo
            case 'k': self.cursor.mover_arriba
            case 'l': return cursor.posicion[0]

@dataclass
class InputHandler:
    cursor: Cursor

    def kb(self):
        opt = readkey()
        dispatch = {
                'j': self.cursor.mover_abajo,
                'k': self.cursor.mover_arriba,
                'h': sys.exit,
                'q': sys.exit
                }
        if opt in dispatch:
            dispatch[opt]()
            return (opt)
        else:
            print("opcion inválida")
@dataclass
class Controller:
    menu_stack: list[MenuView0] = field(default_factory=lambda:[MenuView0()])
    
    # def getInput(self, value):


def main():
    menu0 = MenuView0()
    # menu0.cursor.posicion = (3,2)
    menu_stack = [menu0]
    inputkb = InputHandler(menu_stack[-1].cursor)
    while True:
        Terminal.reiniciar_pantalla()
        Terminal.ocultar_cursor()
        menu_stack[-1].render()
        inputkb.kb()


if __name__ == "__main__":
    main()
