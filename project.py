from dataclasses import dataclass, field
from modules.terminal import Terminal


@dataclass
class Cursor:
    symbol: str = '>'
    linea: int = 0
    columna: int = 0
    max_posicion: tuple[int, int] = (10, 0)

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
class MenuView0:
    cursor: Cursor=field(default_factory=lambda:Cursor(max_posicion=(1,0)))
    opt: list=field(default_factory=lambda:["1. opt a", "2. opt b"])

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
class InputHandler:
    cursor: Cursor
    #: list=field(default_factory=lambda:[])

    def kb(self):
        opt = input("Ingresa Opción")
        match opt:
            case 'j':
                print("presionaste j!")
                self.cursor.mover_abajo()
            case 'k':
                print("presionaste k!")
                self.cursor.mover_arriba()

        return (opt)

def main():
    menu = MenuView0()
    inputkb = InputHandler(menu.cursor)
    while True:
        Terminal.reiniciar_pantalla()
        menu.render()
        inputkb.kb()

if __name__ == "__main__":
    main()
