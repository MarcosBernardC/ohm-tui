def normalizar(numero, unidad) -> str:
    si_exp = {
            -9: 'n',
            -6: 'u',
            -3: 'm',
            0: '',
            3: 'k',
            6: 'M',
            9: 'G'
            }

    mantisa_min = 1
    mantisa_max = 999

    exponente = 0

    if numero != 0:
        while numero <= mantisa_min:
            numero *= 1000
            exponente -= 3

        while numero >= mantisa_max:
            numero /= 1000
            exponente += 3

    return(f"{numero:.2f} {si_exp[exponente]}{unidad}")

def main():
    unidad = 'A'
    entrada = float(input("Ingrese número de ejemplo: "))

    norm_str = normalizar(entrada, unidad)

    print(f"Valor normalizado: {norm_str}")

if __name__ == "__main__":
    main()
