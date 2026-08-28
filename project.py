from src.core.terminal import Terminal
from src.core.input import InputHandler


def main():
    input_handler = InputHandler()

    lista_menu = [10*'-', "Example", 10*'-', "Val 1 : ", "Val 2 : "]
    while True:
        Terminal.limpiar_pantalla()
        Terminal.mover_cursor(1, 1)
        menu_str = '\n'.join(lista_menu)
        print(menu_str)
        kb = input_handler.kb()
        print(f"Haz presionado {kb}!")
        if kb in ['e', 'E']:
            print("modo editar")
            Terminal.mover_cursor(4, 9)
            input()


if __name__ == "__main__":
    main()
