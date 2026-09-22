from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, InvalidOperation


@dataclass
class Corriente:
    unidad: str = 'A'
    valor: Decimal = field(default_factory=lambda : Decimal("0.00"))

@dataclass
class Voltaje:
    unidad: str = 'V'
    valor: Decimal = field(default_factory=lambda : Decimal("0.00"))

@dataclass
class Resistencia:
    unidad: str = 'Ω'
    valor: Decimal = field(default_factory=lambda: Decimal("0.00"))

@dataclass
class OhmModel:
    corriente: Corriente = field(default_factory=Corriente)
    voltaje: Voltaje = field(default_factory=Voltaje)
    resistencia: Resistencia = field(default_factory=Resistencia)

    @staticmethod
    def normalizar(parametro):
        si_exp = {
                -30: 'q',
                -27: 'r',
                -24: 'y',
                -21: 'z',
                -18: 'a',
                -15: 'f',
                -12: 'p',
                -9: 'n',
                -6: 'u',
                -3: 'm',
                0: '',
                3: 'k',
                6: 'M',
                9: 'G',
                12: 'T',
                15: 'P',
                18: 'E',
                21: 'Z',
                24: 'Y',
                27: 'R',
                30: 'Q'
                }
  
        mantisa_min = Decimal("1.00")
        mantisa_max = Decimal("1000.00")
        exponente = 0
        mantisa = parametro.valor


        if parametro.valor != Decimal("0") and parametro.valor != "ERR":
            while mantisa < mantisa_min:
                mantisa *= 1000
                exponente -= 3
            while mantisa >= mantisa_max:
                mantisa /= 1000
                exponente += 3

            mantisa = mantisa.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
            
            while mantisa < mantisa_min:
                mantisa *= 1000
                exponente -= 3
            while mantisa >= mantisa_max:
                mantisa /= 1000
                exponente += 3
 
            if exponente <= 30 and exponente >=-30:
                parametro.prefijo_si = si_exp[exponente]
                return(f"{mantisa.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)} {parametro.prefijo_si}{parametro.unidad}")
            else:
                return("ERR")
        elif parametro.valor == Decimal("0"):
            return (f"{Decimal(parametro.valor).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)}")

        else: return (f"ERR")
    
    def calcular(self, unidad):
        match unidad:
            case 'V':
                self.voltaje.valor = abs(self.corriente.valor*self.resistencia.valor)
            case 'A':
                try:
                    self.corriente.valor = abs(self.voltaje.valor/self.resistencia.valor)
                    self.corriente.unidad = 'A'
                except (ZeroDivisionError, InvalidOperation):
                    self.corriente.valor = "ERR"
                    self.corriente.unidad = ''
            case 'R':
                try:
                    self.resistencia.valor = abs(self.voltaje.valor/self.corriente.valor)
                    self.resistencia.unidad = 'Ω'
                except ZeroDivisionError:
                    self.resistencia.valor = "ERR"
                    self.resistencia.unidad = ''
