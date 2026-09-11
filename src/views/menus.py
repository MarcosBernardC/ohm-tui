from dataclasses import dataclass, field
from src.core.cursor import Cursor
from src.models.model import Corriente, Voltaje, Resistencia, OhmModel

@dataclass
class MainMenu:
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(5,1))) 
    banner: list=field(default_factory=lambda:[
        43*'=',
        15*' '+"OHM-TUI v1.0   ",
        43*'=']) 
    opt_str_list: list=field(default_factory=lambda:[
        ("1.", "1. Calcular Voltaje (V = I × R)"),
        ("2.", "2. Calcular Corriente (I = V / R)"),
        ("3.", "3. Calcular Resistencia (R = V / I)"),
        ("4.", "4. Ver Changelog"), 
        ("5.", "5. Ayuda / Atajos")])
    footer: list = field(default_factory=lambda:[
        43*"=", "subir/bajar [k/j] . Entrar [l] . Salir [q]"])

    def render(self):
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            # print(str_opt[1])
            # input()
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt[1]}")
            else:
                menu_str.append(f"  {str_opt[1]}")
        
        for element in self.footer:
            menu_str.append(element)
        
        print('\n'.join(menu_str))

@dataclass
class MenuAyuda:
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(1,1)))
    banner: list=field(default_factory=lambda:[
        26*'=',
        6*' '+"Ayuda / Atajos",
        26*'='])
    opt_str_list: list=field(default_factory=lambda:[
        "[j] Mover abajo    ▼",
        "[k] Mover arriba   ▲",
        "[h] Volver atrás   ◄",
        "[l] Ingresar       ►",
        "[q] Salir"])
    footer: list = field(default_factory=lambda:[
        26*"=", "Volver [h] . Salir [q]"])
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
class MenuChangelog:
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(1,1)))
    banner: list=field(default_factory=lambda:[
        38*'=',
        15*' '+"CHANGELOG",
        38*'='])
    opt_str_list: list=field(default_factory=lambda:[
        '\n'+"v1.1.0 (Actual)",
        "  * feat: agregado panel de historial",
        "  * refactor: unificación de vistas",])
    footer: list = field(default_factory=lambda:[
        '\n'+38*"=", "Volver [h] . Salir [q]"])
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
class MenuCalcularVoltaje:
    modelo: OhmModel = field(default_factory=OhmModel)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[
        36*'=',
        9*' '+"CÁLCULO DE VOLTAJE",
        36*'='])
    opt_str_list: list=field(default_factory=lambda:[
        ("1.1.", "1.1. Corriente (I)     : "),
        ("1.2.", "1.2. Resistencia (R)   :")])
    footer: list=field(default_factory=lambda:[
        40*'-',
            "  Resultado (V)     :",
        40*'=',
        "Editar [l] . Volver [h] . Ayuda [?]"]) 

    def render(self):
        self.opt_str_list = [
            ("1.1.", f"1.1. Corriente (I)    : {self.modelo.corriente.valor} {self.modelo.corriente.unidad}"),
            ("1.2.", f"1.2. Resistencia (R)  : {self.modelo.resistencia.valor} {self.modelo.resistencia.unidad}")]

        self.footer = [
            17*'-',
            f"  Resultado (V)         : {self.modelo.voltaje.valor} {self.modelo.voltaje.unidad}",
            36*'=',
            "Editar [l] . Volver [h] . Ayuda [?]"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt[1]}")
            else:
                menu_str.append(f"  {str_opt[1]}")
        
        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

@dataclass
class MenuCalcularCorriente:
    modelo: OhmModel = field(default_factory=OhmModel)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[
        36*'=',
        7*' '+"CÁLCULO DE CORRIENTE",
        36*'='])
    opt_str_list: list=field(default_factory=lambda:[("2.1.", f"2.1. Voltaje (V):"), ("2.2.", "2.2. Resistencia (R):")])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "Resultado (I)            :",
        18*'-',
        "[Enter] Guardar | [h] Volver / Cancelar"]) 

    def render(self):
        self.opt_str_list = [
            ("2.1.", f"2.1. Voltaje (V)      : {self.modelo.voltaje.valor} {self.modelo.voltaje.unidad}"),
            ("2.2.", f"2.2. Resistencia (R)  : {self.modelo.resistencia.valor} {self.modelo.resistencia.unidad}")]

        self.footer = [
            18*'-',
            f"  Resultado (I)         : {self.modelo.corriente.valor} {self.modelo.corriente.unidad}",
            36*'=',
            "Editar [l] . Volver [h] . Ayuda [?]"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt[1]}")
            else:
                menu_str.append(f"  {str_opt[1]}")

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

@dataclass
class MenuCalcularResistencia:
    modelo: OhmModel = field(default_factory=OhmModel)
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[
        36*'=',
        7*' '+"CÁLCULO DE RESISTENCIA",
        36*'='])
    opt_str_list: list=field(default_factory=lambda:[("3.1", f"3.1. Valor de Voltaje (V) : "), ("3.2.", "3.2. Valor de Corriente (I):")])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "  Resultado (R)            :",
        18*'-',
        "[Enter] Guardar | [h]RVolver / Cancelar"]) 

    def render(self):
        self.opt_str_list = [
            ("3.1.", f"3.1. Voltaje (V)      : {self.modelo.voltaje.valor} {self.modelo.voltaje.unidad}"),
            ("3.2.", f"3.2. Corriente (I)    : {self.modelo.corriente.valor} {self.modelo.corriente.unidad}")]

        self.footer = [
            18*'-',
            f"  Resultado (R)         : {self.modelo.resistencia.valor} {self.modelo.resistencia.unidad}",
            36*'=',
            "Editar [l] . Volver [h] . Ayuda [?]"]
        menu_str = []
        
        for element in self.banner:
            menu_str.append(element)

        cursor_pos = self.cursor.posicion
        init_pos = self.cursor.min_posicion
        for i, str_opt in enumerate(self.opt_str_list):
            if i+init_pos[0] == cursor_pos[0]: #línea (Y)
                menu_str.append(f"{self.cursor.symbol} {str_opt[1]}")
            else:
                menu_str.append(f"  {str_opt[1]}")

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

