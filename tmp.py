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
    # Pruebas de normalización
    resistencia = Resistencia()
    num1 = input()
    if is_Decimal(num1):
        resistencia.valor = Decimal(num1).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    corriente = Corriente()
    num2 = input()
    if is_Decimal(num2):
        corriente.valor = Decimal(num2).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
   
    voltaje = Voltaje()
    voltaje.valor = corriente.valor*resistencia.valor
   
    print(f"corriente = {corriente.valor} {corriente.unidad}\nresistencia = {resistencia.valor} {resistencia.unidad}\nvoltaje = {corriente.valor*resistencia.valor} {voltaje.unidad}")

    print(f"type(voltaje.valor): {type(voltaje.valor)}")

    voltaje_redondeado = voltaje.valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(f"voltaje redondeado: {voltaje_redondeado}")

if __name__ == "__main__":
    main()
