from readchar import readkey
import sys
from dataclasses import dataclass, field
from src.core.cursor import Cursor
from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.views.menus import MainMenu, MenuAyuda, MenuCalcularVoltaje, MenuCalcularCorriente, MenuCalcularResistencia, MenuMostrarParametros


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    return 

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
        # print(menu.opt_str_list[cursor_rel_pos].split()[0])
        match menu.opt_str_list[cursor_rel_pos].split()[0]:
        # Menu 1.0: ====
            case "1.":
                self.menu_stack.append(MenuCalcularVoltaje())
            case "1.1.":                
                print("menu: 1.1.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(4, 33)
                value = input()
                if is_float(value):
                    menu.corriente.valor = float(value)
                    menu.voltaje.valor = menu.corriente.valor*menu.resistencia.valor
                else:
                    print("Valor inválido")                    
            case "1.2.":
                print("menu: 1.2.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(5, 34)
                value = input()
                if is_float(value):
                    menu.resistencia.valor = float(value)
                    menu.voltaje.valor = menu.corriente.valor*menu.resistencia.valor
                else:
                    print("Valor inválido")
        # Menu 2.0: ====
            case "2.":
                print("menu: 2.")
                self.menu_stack.append(MenuCalcularCorriente())    
            case "2.1.":                
                print("menu: 2.1.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(4, 31)
                value = input()
                if is_float(value):
                    menu.voltaje.valor = float(value)
                    try:
                        menu.corriente.valor = menu.voltaje.valor/menu.resistencia.valor
                        menu.corriente.unidad = 'A'
                    except ZeroDivisionError:
                        menu.corriente.valor = "ERR"
                        menu.corriente.unidad = ''
                else:
                    print("Valor inválido")                    
            case "2.2.":
                print("menu: 2.2.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(5, 34)
                value = input()
                if is_float(value):
                    menu.resistencia.valor = float(value)
                    try:
                        menu.corriente.valor = menu.voltaje.valor/menu.resistencia.valor
                        menu.corriente.unidad = 'A'
                    except ZeroDivisionError:
                        menu.corriente.valor = "ERR"
                        menu.corriente.unidad = ''
                else:
                    print("Valor inválido")                    

        # Menu 3.0: ====
            case "3.":
                print("menu: 3.")
                self.menu_stack.append(MenuCalcularResistencia())    
            case "3.1.":                
                print("menu: 3.1.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(4, 31)
                value = input()
                if is_float(value):
                    menu.voltaje.valor = float(value)
                    try:
                        menu.resistencia.valor = menu.voltaje.valor/menu.corriente.valor
                        menu.resistencia.unidad = 'Ω'
                    except ZeroDivisionError:
                        menu.resistencia.valor = "ERR"
                        menu.resistencia.unidad = ''
                else:
                    print("Valor inválido")                    
            case "3.2.":
                print("menu: 3.2.")
                Terminal.mostrar_cursor()
                Terminal.mover_cursor(5, 32)
                value = input()
                if is_float(value):
                    menu.corriente.valor = float(value)
                    try:
                        menu.resistencia.valor = menu.voltaje.valor/menu.corriente.valor
                        menu.resistencia.unidad = 'Ω'
                    except ZeroDivisionError:
                        menu.resistencia.valor = "ERR"
                        menu.resistencia.unidad = ''
                else:
                    print("Valor inválido")                    
        # Menu 4.0: ====
            case "4.":
                self.menu_stack.append(MenuMostrarParametros())    
            case "5.":
                print("menu: Ayuda")
                self.menu_stack.append(MenuAyuda())
        print(f"Menú seleccionado: {menu.opt_str_list[cursor_rel_pos]}")
        #input()

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
