def main():
    unidad = 'A'
    si_exp = {
            -9: 'n',
            -6: 'u',
            -3: 'm',
            0: '',
            3: 'k',
            6: 'M',
            9: 'G'
            }


    entrada = float(input("Ingrese número de ejemplo: "))
    tmp = entrada

    mantisa_min = 1
    mantisa_max = 999

    exponente = 0

    if entrada != 0:
        while entrada <= mantisa_min:
            entrada *= 1000
            exponente -= 3

        while entrada >= mantisa_max:
            entrada /= 1000
            exponente += 3

    

    print(f"Valores normalizados:\n - entrada: {tmp}\n - entrada normalizada: {entrada:.2f}\n - exponente: {exponente}\n - si_exp: {si_exp[exponente]}\n Resultado: {entrada:.2f} {si_exp[exponente]}{unidad}")


if __name__ == "__main__":
    main()
