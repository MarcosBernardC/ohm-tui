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
        self.voltaje.valor = abs(self.corriente.valor*self.resistencia.valor)

    def calcular_corriente(self):
        try:
            self.corriente.valor = abs(self.voltaje.valor/self.resistencia.valor)
            self.corriente.unidad = 'A'
        except ZeroDivisionError:
            self.corriente.valor = "ERR"
            self.corriente.unidad = ''

    def calcular_resistencia(self):
        try:
            self.resistencia.valor = abs(self.voltaje.valor/self.corriente.valor)
            self.resistencia.unidad = 'Ω'
        except ZeroDivisionError:
            self.resistencia.valor = "ERR"
            self.resistencia.unidad = ''

    @staticmethod
    def normalizar(parametro):
        si_exp = {
                -9: 'n',
                -6: 'u',
                -3: 'm',
                0: '',
                3: 'k',
                6: 'M',
                9: 'G'
                }

        mantisa_min = 1
        mantisa_max = 999
        exponente = 0

        numero = parametro.valor # evita romper el valor original del dato
        
        if numero != 0 and numero != "ERR":
            while numero <= mantisa_min:
                numero *= 1000
                exponente -= 3
            while numero >= mantisa_max:
                numero /= 1000
                exponente += 3
            parametro.prefijo_si = si_exp[exponente]
            return(f"{numero:.2f} {parametro.prefijo_si}{parametro.unidad}")
        return (f"{parametro.valor}")
