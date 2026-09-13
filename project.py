from src.core.terminal import Terminal
from src.core.input import InputHandler
from src.controllers.app_controller import Controller


def mover_cursor(secuencia_entrada: list[str]) -> tuple[int, int]:
    controller = Controller()
    
    for tecla_entrada in secuencia_entrada:
        controller.exec_kb(tecla_entrada)
     
    return controller.menu_stack[-1].cursor.posicion 

def navegar(secuencia_entrada: list[str]) -> str:
    controller = Controller()
    
    for tecla_entrada in secuencia_entrada:
        controller.exec_kb(tecla_entrada)
    if controller.menu_stack[-1].navigable:
        return controller.menu_stack[-1].opt_str_list[controller.menu_stack[-1].cursor.rel_posicionY][0]
    else:
        return controller.menu_stack[-1].banner[1].strip()
        
def calcular_parametro(secuencia_entrada: list[str], valor1: float, valor2: float, parametro: str):
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.exec_kb(tecla_entrada)

    match parametro:
        case "voltaje":
            controller.menu_stack[-1].modelo.corriente.valor = valor1
            controller.menu_stack[-1].modelo.resistencia.valor = valor2
             
            controller.menu_stack[-1].modelo.calcular_voltaje()

            return controller.menu_stack[-1].modelo.voltaje.valor
        case "corriente":
            controller.menu_stack[-1].modelo.voltaje.valor = valor1
            controller.menu_stack[-1].modelo.resistencia.valor = valor2
             
            controller.menu_stack[-1].modelo.calcular_corriente()

            return controller.menu_stack[-1].modelo.corriente.valor
        case "resistencia":
            controller.menu_stack[-1].modelo.voltaje.valor = valor1
            controller.menu_stack[-1].modelo.corriente.valor = valor2
             
            controller.menu_stack[-1].modelo.calcular_resistencia()

            return controller.menu_stack[-1].modelo.resistencia.valor
            

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
