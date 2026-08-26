from dataclasses import dataclass, field
from src.core.cursor import Cursor

@dataclass
class MainMenu: #main menu
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(3,1)))
    banner: list=field(default_factory=lambda:[15*'-', "Main Menu", 15*'-'])
    opt_str_list: list=field(default_factory=lambda:["Opt1", "Opt2", "Ayuda"])

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
    banner: list=field(default_factory=lambda:[15*'-', "Help Menu", 15*'-'])
    opt_str_list: list=field(default_factory=lambda:["[j] Mover abajo", "[k] Mover arriba", "[h] Volver atrás", "[q] Salir", "[l] Ingresar"])
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

        print('\n'.join(menu_str))
