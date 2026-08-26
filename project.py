from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.controllers.app_controller import Controller


def main():
    inputkb = InputHandler()
    controller = Controller()

    while True:
        Terminal.reiniciar_pantalla()
        Terminal.ocultar_cursor()
        
        controller.gestionar_menu()
        opt = inputkb.kb()
        controller.exec_kb(opt)


if __name__ == "__main__":
    main()
