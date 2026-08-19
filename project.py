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
        menu_str = []
        for i, str_opt in enumerate(self.opt):
            if i == self.cursor.linea:
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(str_opt)

        print('\n'.join(menu_str))

def main():
    # Terminal.mover_cursor(7,7)
    # print("Línea 7, Columna 7!")

    # cursor = Cursor()
    # print(cursor)
    # print(cursor.posicion)
    #
    # cursor.mover_abajo()
    # print(cursor)
    # print(cursor.posicion)

    menu = MenuView0()
    menu.render()

if __name__ == "__main__":
    main()
