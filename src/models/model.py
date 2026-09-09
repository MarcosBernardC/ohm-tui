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
