from dataclasses import dataclass, field

@dataclass
class Corriente:
    unidad: str = 'A'
    valor: float = 0.0

@dataclass
class Voltaje:
    unidad: str = 'V'
    valor: float = 0.0

@dataclass
class Resistencia:
    unidad: str = 'Ω'
    valor: float = 0.0

@dataclass
class OhmModel:
    corriente: Corriente = field(default_factory=Corriente)
    voltaje: Voltaje = field(default_factory=Voltaje)
    resistencia: Resistencia = field(default_factory=Resistencia)

    def calcular_voltaje(self):
        self.voltaje.valor = self.corriente.valor*self.resistencia.valor

    def calcular_corriente(self):
        try:
            self.corriente.valor = self.voltaje.valor/self.resistencia.valor
            self.corriente.unidad = 'A'
        except ZeroDivisionError:
            self.corriente.valor = "ERR"
            self.corriente.unidad = ''

    def calcular_resistencia(self):
        try:
            self.resistencia.valor = self.voltaje.valor/self.corriente.valor
            self.resistencia.unidad = 'Ω'
        except ZeroDivisionError:
            self.resistencia.valor = "ERR"
            self.resistencia.unidad = ''




