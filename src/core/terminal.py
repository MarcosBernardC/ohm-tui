# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
class Terminal:
    @staticmethod
    def _imprimir_secuencia(secuencia):
        print(secuencia, end='', flush=True)           
    
    @staticmethod
    def limpiar_pantalla() -> None:
        Terminal._imprimir_secuencia("\033[2J")
    
    @staticmethod
    def mover_cursor(line, column) -> None:
        Terminal._imprimir_secuencia(f"\033[{line};{column}f")

    @staticmethod
    def ocultar_cursor() -> None:
        Terminal._imprimir_secuencia("\033[?25l")

    @staticmethod
    def reiniciar_pantalla() -> None:
        Terminal.limpiar_pantalla()
        Terminal.mover_cursor(0,0)

if __name__ == "__main__":
    pass
