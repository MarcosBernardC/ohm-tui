from readchar import readkey
import sys
from dataclasses import dataclass, field
from modules.terminal import Terminal


class Cursor:
    def __init__(self,
                 symbol: str = '>',
                 max_posicion: tuple[int, int] = (10, 1),
                 min_posicion: tuple[int, int] = (1, 1),
                 linea: int = None,
                 columna: int = None):
        self.symbol = symbol
        self.max_posicion = max_posicion
        self.min_posicion = min_posicion
        self.linea = min_posicion[0]
        self.columna = min_posicion[1]

    def mover_arriba(self):
        if self.linea > self.min_posicion[0]:
            self.linea -= 1
    
    def mover_abajo(self):
        if self.linea < self.max_posicion[0]:
            self.linea += 1

    def mover_derecha(self):
        if self.columna < self.max_posicion[1]:
            self.columna += 1

    def mover_izquierda(self):
        if self.columna > self.min_posicion[1]:
            self.columna -= 1

    @property
    def posicion(self):
        return (self.linea, self.columna)

    @posicion.setter
    def posicion(self, value: tuple[int, int]):
        self.linea = value[0]
        self.columna = value[0]

    @property
    def rel_posicionY(self):
        return self.linea-self.min_posicion[0]
    
@dataclass
class MenuView0: #main menu
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

@dataclass
class MenuEditarVoltaje:
    cursor: Cursor=field(default_factory=lambda:Cursor(min_posicion=(1, 1), max_posicion=(2,1)))
    banner: list=field(default_factory=lambda:[15*'-', "Editar: Voltaje", 15*'-'])
    opt_str_list: list=field(default_factory=lambda:["Valor anterior : ", "Nuevo valor    : "])
    footer: list=field(default_factory=lambda:["\n[Enter] Guardar | [h] Volver / Cancelar"])

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

    # def handle_input(self, value):
    #     match value:
    #         case 'j': self.cursor.mover_abajo
    #         case 'k': self.cursor.mover_arriba

@dataclass
class InputHandler:
    def kb(self):
        opt = readkey()
        return (opt)

@dataclass
class Controller:
    menu_stack: list[MenuView0] = field(default_factory=lambda:[MenuView0()]) 

    def exec_kb(self, value):
        menu = self.menu_stack[-1]
        print(f"Opción actual: {menu.cursor.rel_posicionY}")
        dispatch = {
                'j': menu.cursor.mover_abajo,
                'k': menu.cursor.mover_arriba,
                'l': self.add_menu,
                'h': self.delete_menu,
                'q': self.quit,
                '?': self.help_menu
                }
        if value in dispatch:
            cursor = menu.cursor
            # print(f"Posición cursor: {cursor.posicion[0]}")
            # print(f"Opción: {cursor.rel_posicionY}")
            # print(f"Opción actual: {menu.opt_str_list[cursor.rel_posicionY]}")
            dispatch[value]()
        else:
            print("opcion inválida")
        print(value)
        #input()

    def help_menu(self):
        if isinstance(self.menu_stack[-1], MenuAyuda):
            return 0
        else:
            self.menu_stack.append(MenuAyuda())

    def add_menu(self):
        menu = self.menu_stack[-1]
        cursor_rel_pos = menu.cursor.rel_posicionY
        match menu.opt_str_list[cursor_rel_pos]:
            case "Opt1":
                print("menu: Opt1")
                self.menu_stack.append(MenuEditarVoltaje())
            case "Opt2":
                print("menu: Opt2")
            case "Ayuda":
                print("menu: Ayuda")
                self.menu_stack.append(MenuAyuda())

    def gestionar_menu(self):
        self.menu_stack[-1].render()

    def delete_menu(self):
        cantidad_menus = len(self.menu_stack)
        if cantidad_menus > 1:
            print(f"Longitud menús: {cantidad_menus}")
            self.menu_stack.pop()

    def quit(self):
        tmp = input("\n¿Salir del programa? (y/N): ")
        if tmp == 'y' or tmp == 'Y':
            sys.exit()

def main():
    menu0 = MenuView0()
    # menu0.cursor.posicion = (3,2)
    menu_stack = [menu0]
    inputkb = InputHandler()
    controller = Controller()

    while True:
        Terminal.reiniciar_pantalla()
        Terminal.ocultar_cursor()
        
        controller.gestionar_menu()
        # menu_stack[-1].render()
        opt = inputkb.kb()
        controller.exec_kb(opt)


if __name__ == "__main__":
    main()
