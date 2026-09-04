from dataclasses import dataclass

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

class OhmModel:
    def __init__(self, corriente: Corriente, voltaje: Voltaje, resistencia: Resistencia):
        self.corriente = corriente
        self.voltaje = voltaje
        self.resistencia = resistencia
    
    def __str__(self):
        return f"Corriente: {self.corriente.valor} {self.corriente.unidad}\nResistencia: {self.resistencia.valor} {self.resistencia.unidad}\nVoltaje: {self.voltaje.valor} {self.voltaje.unidad}"

