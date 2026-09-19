from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

@dataclass
class Voltaje:
    unidad: str = 'V'
    valor: Decimal = field(default_factory=lambda: Decimal("0.00"))

@dataclass
class Resistencia:
    unidad: str = "Ω"
    valor: Decimal = field(default_factory=lambda: Decimal("0.00"))

@dataclass
class Corriente:
    unidad: str = 'A'
    valor: Decimal = field(default_factory=lambda: Decimal("0.00"))

def is_Decimal(valor):
    try:
        Decimal(valor)
        return True
    except InvalidOperation:
        return False


def main():
    pass

if __name__ == "__main__":
    main()
