from dataclasses import dataclass, field
from src.core.cursor import Cursor

@dataclass
class MainMenu: #main menu
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(5,1)))
    banner: list=field(default_factory=lambda:[18*'-', "   OHM-TUI v1.0   ", 18*'-'])
    opt_str_list: list=field(default_factory=lambda:[
        "1. Calcular Voltaje (V = I × R)",
        "2. Calcular Corriente (I = V / R)",
        "3. Calcular Resistencia (R = V / I)",
        "4. Configurar Parámetros", 
        "5. Ayuda / Atajos"])

    def render(self):
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(f"  {str_opt}")

        print('\n'.join(menu_str))

@dataclass
class MenuAyuda: #main menu
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(1,1)))
    banner: list=field(default_factory=lambda:[17*'-', " Ayuda / Atajos  ", 17*'-'])
    opt_str_list: list=field(default_factory=lambda:["[j] Mover abajo", "[k] Mover arriba", "[h] Volver atrás", "[q] Salir", "[l] Ingresar"])
    footer: list = field(default_factory=lambda:[
        17*"-", "Presione [h] para volver"])
    navigable: bool = False

    def render(self):
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion

        if self.navigable == True:
            for i, str_opt in enumerate(self.opt_str_list):
                if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                    menu_str.append(f"{self.cursor.symbol} {str_opt}")
                else:
                    menu_str.append(f"  {str_opt}")
        else:
            for i, str_opt in enumerate(self.opt_str_list):
                menu_str.append(f"{str_opt}")

        for element in self.footer:
            menu_str.append(element)
        
        print('\n'.join(menu_str))


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
class MenuCalcularVoltaje:
    corriente: Corriente = field(default_factory=lambda:Corriente)
    voltaje: Voltaje = field(default_factory=Voltaje)
    resistencia: Resistencia = field(default_factory=Resistencia)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[18*'-', "Cálculo de Voltaje", 18*'-'])
    opt_str_list: list=field(default_factory=lambda:[f"1.1. Valor de Corriente (I) : ", "1.2. Valor de Resistencia (R):"])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "Resultado (V)            :",
        18*'-',
        "[Enter] Guardar | [h] Volver / Cancelar"]) 

    def render(self):
        self.opt_str_list = [f"1.1. Valor de Corriente (I) : {self.corriente.valor} {self.corriente.unidad}", f"1.2. Valor de Resistencia (R): {self.resistencia.valor} {self.resistencia.unidad}"]

        self.footer = [
            18*'-',
            f"Resultado (V)            : {self.voltaje.valor} {self.voltaje.unidad}",
            18*'-',
            "[Enter] Guardar | [h] Volver / Cancelar"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(f"  {str_opt}")

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

@dataclass
class MenuCalcularCorriente:
    corriente: Corriente = field(default_factory=Corriente)
    voltaje: Voltaje = field(default_factory=Voltaje)
    resistencia: Resistencia = field(default_factory=Resistencia)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[20*'-', "Cálculo de Corriente", 20*'-'])
    opt_str_list: list=field(default_factory=lambda:[f"2.1. Valor de Voltaje (V) : ", "2.2. Valor de Resistencia (R):"])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "Resultado (I)            :",
        18*'-',
        "[Enter] Guardar | [h] Volver / Cancelar"]) 

    def render(self):
        self.opt_str_list = [f"2.1. Valor de Voltaje (V) : {self.voltaje.valor} {self.voltaje.unidad}", f"2.2. Valor de Resistencia (R): {self.resistencia.valor} {self.resistencia.unidad}"]

        self.footer = [
            18*'-',
            f"Resultado (I)            : {self.corriente.valor} {self.corriente.unidad}",
            18*'-',
            "[Enter] Guardar | [h] Volver / Cancelar"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(f"  {str_opt}")

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

@dataclass
class MenuCalcularResistencia:
    corriente: Corriente = field(default_factory=Corriente)
    voltaje: Voltaje = field(default_factory=Voltaje)
    resistencia: Resistencia = field(default_factory=Resistencia)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[20*'-', "Cálculo de Corriente", 20*'-'])
    opt_str_list: list=field(default_factory=lambda:[f"3.1. Valor de Voltaje (V) : ", "3.2. Valor de Corriente (I):"])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "Resultado (R)            :",
        18*'-',
        "[Enter] Guardar | [h]RVolver / Cancelar"]) 

    def render(self):
        self.opt_str_list = [f"3.1. Valor de Voltaje (V) : {self.voltaje.valor} {self.voltaje.unidad}", f"3.2. Valor de Corriente (I): {self.corriente.valor} {self.corriente.unidad}"]

        self.footer = [
            18*'-',
            f"Resultado (R)            : {self.resistencia.valor} {self.resistencia.unidad}",
            18*'-',
            "[Enter] Guardar | [h] Volver / Cancelar"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt}")
            else:
                menu_str.append(f"  {str_opt}")

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))
