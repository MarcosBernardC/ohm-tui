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
class MenuCalcularVoltaje:
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[18*'-', "   Cálculo de Voltaje   ", 18*'-'])
    opt_str_list: list=field(default_factory=lambda:["Valor de Corriente (I) : ", "Valor de Resistencia (R): "])
    footer: list=field(default_factory=lambda:[
        18*'-',
        "Resultado (V)            :",
        18*'-',
        "[Enter] Guardar | [h] Volver / Cancelar"])

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

        for element in self.footer:
            menu_str.append(element)

        print('\n'.join(menu_str))

