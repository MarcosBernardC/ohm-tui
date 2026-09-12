from readchar import readkey
import sys
from dataclasses import dataclass, field
# from src.core.cursor import Cursor
from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.views.menus import MainMenu, MenuAyuda, MenuCalcularVoltaje, MenuCalcularCorriente, MenuCalcularResistencia, MenuChangelog, OhmModel


@dataclass
class Controller:
    menu_stack: list[MainMenu] = field(default_factory=lambda:[MainMenu()])
    
    def exec_kb(self, value):
        menu = self.menu_stack[-1]
        #print(f"Opción actual: {menu.cursor.rel_posicionY}")
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


    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def edit_value(self, cursor_edit_position: tuple[int, int], edit_obj: object, edit_param: str):
        Terminal.mostrar_cursor()
        Terminal.mover_cursor(cursor_edit_position[0], cursor_edit_position[1])
        value = input()
        if Controller.is_float(value):
            valor_a_editar = float(value)
            setattr(edit_obj, edit_param, valor_a_editar)
        else:
            print("valor inválido")

    def add_menu(self):
        menu = self.menu_stack[-1]
        cursor_rel_pos = menu.cursor.rel_posicionY
        opt = menu.opt_str_list[cursor_rel_pos]
        idmenu = opt[0]
        # print(opt)
        # input()
        match idmenu:
        # Menu 1.0: ====
            case "1.":
                # print(f"IDmenu: {idmenu}")
                self.menu_stack.append(MenuCalcularVoltaje())
            case "1.1.":                
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(4,27), edit_obj=menu.modelo.corriente, edit_param="valor")
                menu.modelo.voltaje.valor = menu.modelo.corriente.valor*menu.modelo.resistencia.valor
            case "1.2.":
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(5, 27), edit_obj=menu.modelo.resistencia, edit_param="valor")
                menu.modelo.calcular_voltaje()
        # Menu 2.0: ====
            case "2.":
                # print(f"IDmenu: {idmenu}")
                self.menu_stack.append(MenuCalcularCorriente())    
            case "2.1.":                
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(4, 27), edit_obj=menu.modelo.voltaje, edit_param="valor")
                menu.modelo.calcular_corriente()
            case "2.2.":
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(5,27), edit_obj=menu.modelo.resistencia, edit_param="valor")
                menu.modelo.calcular_corriente()
        # Menu 3.0: ====
            case "3.":
                # print(f"IDmenu: {idmenu}")
                self.menu_stack.append(MenuCalcularResistencia())    
            case "3.1.":                
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(4,27), edit_obj=menu.modelo.voltaje, edit_param="valor")
                menu.modelo.calcular_resistencia()
            case "3.2.":
                # print(f"IDmenu: {idmenu}")
                self.edit_value(cursor_edit_position=(5,27), edit_obj=menu.modelo.corriente, edit_param="valor")
                menu.modelo.calcular_resistencia()
        # Menu 4.0: ====
            case "4.":
                # print(f"IDmenu: {idmenu}")
                self.menu_stack.append(MenuChangelog())
            case "5.":
                # print(f"IDmenu: {idmenu}")
                self.menu_stack.append(MenuAyuda()) 
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
