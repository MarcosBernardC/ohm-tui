from src.controllers.app_controller import Controller


def main():
    controller = Controller()

    while True: 
        controller.gestionar_menu()
        controller.read_kb()
        controller.exec_kb()


def mover_cursor(secuencia_entrada: list[str]) -> tuple[int, int]:
    controller = Controller()
     
    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()
     
    return controller.menu_stack[-1].cursor.posicion 

det navegar(secuencia_entrada: list[str]) -> str:
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()
    if controller.menu_stack[-1].navigable:
        return controller.menu_stack[-1].opt_str_list[controller.menu_stack[-1].cursor.rel_posicionY][0]
    else:
        return controller.menu_stack[-1].banner[1].strip()

def calcular_parametro(secuencia_entrada: list[str], valor1: float, valor2: float, parametro: str):
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()

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

def normalizar_parametro(secuencia_entrada: list[str], nombre_parametro: str, valor: float) -> str:
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()

    modelo = controller.menu_stack[-1].modelo

    match(nombre_parametro):
        case "corriente":
            corriente = modelo.corriente
            corriente.valor = valor
            return(modelo.normalizar(corriente))

        case "voltaje":
            voltaje = modelo.voltaje 
            voltaje.valor = valor
            return(modelo.normalizar(voltaje))
        case "resistencia":
            resistencia = modelo.resistencia
            resistencia.valor = valor
            return(modelo.normalizar(resistencia))
       

if __name__ == "__main__":
    main()
