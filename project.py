from dataclasses import dataclass
from modules.terminal import Terminal

@dataclass
class Cursor:
    linea: int = 0
    columna: int = 0
    max_posicion: tuple[int, int] = (10, 10)

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
    def posicion(self) -> tuple[int, int]:
        return (self.linea, self.columna)

    @posicion.setter
    def posicion(self, posicion: tuple[int, int]):
        if ((0 <= posicion[0] <= self.max_posicion[0]) and 0 <= posicion[1] <= self.max_posicion[1]):
            linea, columna = posicion
            self.linea = linea
            self.columna = columna

def main():
    # Terminal.mover_cursor(7,7)
    # print("Línea 7, Columna 7!")

    cursor = Cursor()
    print(cursor)
    print(cursor.posicion)

    cursor.mover_abajo()
    print(cursor)
    print(cursor.posicion)

if __name__ == "__main__":
    main()
