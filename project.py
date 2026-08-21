from readchar import readkey
import sys
from dataclasses import dataclass, field
from modules.terminal import Terminal


@dataclass
class Cursor:
    symbol: str = '>'
    linea: int = 1
    columna: int = 1
    max_posicion: tuple[int, int] = (10, 1)
    init_pos: tuple[int, int] = (1, 1)

    def mover_arriba(self):
        if self.linea > 0:
            self.linea -= 1
    
    def mover_abajo(self):
        if self.linea < self.max_posicion[0]:
            self.linea += 1

    def mover_derecha(self):
        if self.columna < self.max_posicion[1]:
            self.columna += 1

    def mover_izquierda(self):
        if self.columna > 0:
            self.columna -= 1

    @property
    def posicion(self):
        return (self.linea, self.columna)

    @posicion.setter
    def posicion(self, value):
        pass

@dataclass
class MenuView0: #main menu
    cursor: Cursor=field(default_factory=lambda:Cursor(max_posicion=(1,1)))
    opt: list=field(default_factory=lambda:["1. Editar", "2. Ayuda"])

    def render(self): 
        cursor_pos = self.cursor.posicion
        menu_str = []
        for i, str_opt in enumerate(self.opt):
            if i == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(str_opt)

        print('\n'.join(menu_str))

@dataclass
class MenuView01: #help menu
    cursor: Cursor=field(default_factory=lambda:Cursor(max_posicion=(1,1)))
    menu_list: list=field(default_factory=lambda:[15*'-',"Ayuda", 15*'-', '', "MOVIMIENTOS BÁSICOS:", "  j - Mover cursor hacia abajo", "  k - Mover cursor hacia arriba"])

    def render(self): 
        for i, str_opt in enumerate(self.menu_list):
            if i == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(str_opt)

        print('\n'.join(menu_str))

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
        dispatch[opt]()
        return (opt)

def main():
    menu0 = MenuView0()
    menu01 = MenuView01()
    menu_list = [menu0]
    inputkb = InputHandler(menu_list[-1].cursor)
    while True:
        Terminal.reiniciar_pantalla()
        menu_list[-1].render()
        inputkb.kb()


if __name__ == "__main__":
    main()
