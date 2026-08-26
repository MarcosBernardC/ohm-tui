from readchar import readkey
import sys
from dataclasses import dataclass, field
from src.core.cursor import Cursor
from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.views.menus import MainMenu, MenuAyuda, MenuEditarVoltaje


@dataclass
class Controller:
    menu_stack: list[MainMenu] = field(default_factory=lambda:[MainMenu()]) 

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
