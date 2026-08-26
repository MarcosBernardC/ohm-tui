class Cursor:
    def __init__(self,
                 symbol: str = '>',
                 max_posicion: tuple[int, int] = (10, 1),
                 min_posicion: tuple[int, int] = (1, 1),
                 linea: int = None,
                 columna: int = None):
        self.symbol = symbol
        self.max_posicion = max_posicion
        self.min_posicion = min_posicion
        self.linea = min_posicion[0]
        self.columna = min_posicion[1]

    def mover_arriba(self):
        if self.linea > self.min_posicion[0]:
            self.linea -= 1
    
    def mover_abajo(self):
        if self.linea < self.max_posicion[0]:
            self.linea += 1

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

    @property
    def rel_posicionY(self):
        return self.linea-self.min_posicion[0]
