from readchar import readkey
import sys
from dataclasses import dataclass, field
from src.core.cursor import Cursor
from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.views.menus import MainMenu, MenuAyuda


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
            case "Configurar valores":
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
