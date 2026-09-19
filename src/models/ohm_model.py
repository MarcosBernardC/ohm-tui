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

    def calcular(self, unidad):
        match unidad:
            case 'V':
                self.voltaje.valor = abs(self.corriente.valor*self.resistencia.valor)
            case 'A':
                try:
                    self.corriente.valor = abs(self.voltaje.valor/self.resistencia.valor)
                    self.corriente.unidad = 'A'
                except ZeroDivisionError:
                    self.corriente.valor = "ERR"
                    self.corriente.unidad = ''
            case 'R':
                try:
                    self.resistencia.valor = abs(self.voltaje.valor/self.corriente.valor)
                    self.resistencia.unidad = 'Ω'
                except ZeroDivisionError:
                    self.resistencia.valor = "ERR"
                    self.resistencia.unidad = ''


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
  
        mantisa = round(parametro.valor, 2)
 
        mantisa_min = 1.00
        mantisa_max = 1000.00
        exponente = 0
    
        if mantisa != 0 and mantisa != "ERR":
            while mantisa <= mantisa_min:
                mantisa *= 1000
                exponente -= 3
            while mantisa >= mantisa_max:
                mantisa /= 1000
                exponente += 3
            if exponente <= 30 and exponente >=-30:
                parametro.prefijo_si = si_exp[exponente]
                return(f"{mantisa:.2f} {parametro.prefijo_si}{parametro.unidad}")
            else:
                return(f"ERR")
        return (f"{parametro.valor}")
