from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def nivel0(): 
    ## Suma normal (con erroresde acarreo natural del sistema)
    suma_normal = 0.1 + 0.1 + 0.1

    suma_Decimal = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")

    print(f"suma_normal: {suma_normal}\nsuma_Decimal: {suma_Decimal}\n")

    
    ## Paso de valores a Decimal
    float_simple = 4.56

    Decimal_float = Decimal(4.56)
    
    Decimal_str = Decimal("4.56")

    print(f"float_simple: {float_simple!r}\nDecimal_float: {Decimal_float}\nDecimal_str: {Decimal_str}\n")

    
    ## Operacioneis aritméticas básicas: decimal
    precio_total = Decimal("0.1")
    cantidad = Decimal("3")
 
    total_unitario = precio_total/cantidad

    print(f"version Decimal:\n----\nprecio_total: {precio_total}\ncantidad: {cantidad}\n---\ntotal_unitario: {total_unitario}\n")
    
    ## Operacioneis aritméticas básicas: float
    precio_total = 0.1
    cantidad = 3
 
    total_unitario = precio_total/cantidad

    print(f"version float:\n----\nprecio_total: {precio_total}\ncantidad: {cantidad}\n---\ntotal_unitario: {total_unitario}\n")

# REDONDEO ROUND_HALF_UP
    print("REDONDEO ROUND_HALF_UP")
 
    total_unitario = Decimal("2.5").quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    print(f"- Version Decimal: {total_unitario}")

# REDONDEO ROUND
    total_unitario = round(2.5, 0)

    print(f"- Version round: {total_unitario}\n")

# REDONDEO ROUND_HALF_EVEN
    print("REDONDEO ROUND_HALF_EVEN") 
    total_unitario = Decimal("2.5").quantize(Decimal("0"), rounding=ROUND_HALF_EVEN)
    print(f"- Version Decimal: {total_unitario}")

# REDONDEO ROUND
    total_unitario = round(2.5, 0)
    print(f"- Version round: {total_unitario}\n")

# Ejercicios:
'''
Nivel 1: Calibración y Promedio en Balanza Analítica

    Contexto: Estás procesando un conjunto de lecturas de masa repetidas obtenidas de una balanza analítica para verificar la repetibilidad del instrumento.

    Consigna:

        Define una lista en Python con los siguientes valores en formato Decimal: ["10.0255", "10.0245", "10.0255", "10.0265"].

        Calcula la media aritmética exacta sumando todos los valores y dividiéndolos entre la cantidad de elementos, operando exclusivamente con objetos Decimal.

        Aplica .quantize(Decimal("0.001"), rounding=ROUND_HALF_EVEN) al resultado final.

        Compara el valor obtenido frente a hacer la misma operación usando ROUND_HALF_UP y observa el impacto en el tercer decimal.
'''
def nivel1(): # Ver norma ASTM E29
    masas = ["10.0255", "10.0245", "10.0255", "10.0265"]

    total_lecturas = 0
    for masa in masas:
        total_lecturas += Decimal(masa)
     
    media = (total_lecturas/len(masas)).quantize(Decimal("0.001"), rounding=ROUND_HALF_EVEN)
    print(f"media ROUND_HALF_EVEN: {media}")
     
    media = (total_lecturas/len(masas)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
    print(f"media ROUND_HALF_UP: {media}")

'''
Para dominar cómo se comporta Decimal ante estos bordes de desborde, te propongo un mini-ejercicio que puedes añadir a tu archivo temporal:

    Define un Decimal("999.9999") y aplícale .quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN). ¿Qué valor exacto te escupe la terminal? ¿Salta el dígito de las centenas?

    Define un Decimal("0.0009999") y experimenta cómo cambia su escala si decides representarlo ajustando sus decimales significativos.
'''
def nivel2():
    sig_decimals = ["0.1", "0.01", "0.01", "0.001", "0.0001"]
    
    for sig_decimal in sig_decimals:
        num1 = Decimal("999.9999")
        num1_quantizado = num1.quantize(Decimal(sig_decimal), rounding=ROUND_HALF_EVEN)
        print(f"num1: {num1}\nsig decimal: {sig_decimal}\nnum1  quantizado: {num1_quantizado}\n----")


def main():
    #nivel0()
    #nivel1()
    nivel2()

if __name__ == "__main__":
    main()
