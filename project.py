from src.controller import Controller


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

def navegar(secuencia_entrada: list[str]) -> str:
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()

    menu = controller.menu_stack[-1]
    cursor = menu.cursor
    if menu.navigable:
        return menu.opt_str_list[cursor.rel_posicionY][0]
    else:
        return menu.banner[1].strip()

def calcular_parametro(secuencia_entrada: list[str], valor1: float, valor2: float):
    controller = Controller()

    for tecla_entrada in secuencia_entrada:
        controller.kb_val = tecla_entrada
        controller.exec_kb()

    menu = controller.menu_stack[-1]
    parametro = menu.main_param
    modelo = menu.modelo

    match parametro:
        case "V":
            modelo.corriente.valor = valor1
            modelo.resistencia.valor = valor2

            modelo.calcular(parametro)

            return modelo.voltaje.valor
        case "A":
            menu.modelo.voltaje.valor = valor1
            menu.modelo.resistencia.valor = valor2

            menu.modelo.calcular(parametro)

            return menu.modelo.corriente.valor
        case "R":
            menu.modelo.voltaje.valor = valor1
            menu.modelo.corriente.valor = valor2

            menu.modelo.calcular(parametro)

            return menu.modelo.resistencia.valor

def normalizar_parametro(secuencia_entrada: list[str], nombre_parametro: str, valor) -> str:
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
