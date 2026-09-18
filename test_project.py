import pytest
from project import mover_cursor, navegar, calcular_parametro, normalizar_parametro


data_mover_cursor = [
        (['k'], (1, 1)),
        (['k', 'j'], (2, 1)),
        (['k', 'j', 'j'], (3, 1)),
        (['k', 'j', 'j', 'j'], (4, 1)),
        (['k', 'j', 'j', 'j', 'j'], (5, 1)),
        (['k', 'j', 'j', 'j', 'j', 'j', 'j'], (5, 1)),
        ]
@pytest.mark.parametrize("secuencia_de_movimiento, posicion_cursor", data_mover_cursor)
def test_mover_cursor(secuencia_de_movimiento, posicion_cursor):
    posicion_final = mover_cursor(secuencia_de_movimiento)

    assert posicion_final == posicion_cursor

data_nav = [(['k'], "1."),              # MAIN MENU
            (['k', 'j'], "2."),
            (['k', 'j', 'j'], "3."),
            (['k', 'j', 'j', 'j'], "4."),
            (['k', 'j', 'j', 'j', 'j'], "5."),
            (['l', 'k'], "1.1."),       # VOLTAGE MENU
            (['l', 'k', 'j'], "1.2."),
            (['l', 'k', 'j', 'j'], "1.2."),
            (['l', 'k', 'j'], "1.2."),
            (['j', 'l', 'k'], "2.1."),  # CURRENT MENU
            (['j', 'l', 'k', 'j'], "2.2."),
            (['j', 'l', 'k', 'j', 'j'], "2.2."),
            (['j', 'j', 'l', 'k'], "3.1."),  # RESISTANCE MENU
            (['j', 'j', 'l', 'k'], "3.1."),
            (['j', 'j', 'l', 'k', 'j'], "3.2."),
            (['j', 'j', 'l', 'k', 'j', 'j'], "3.2."),
            
            (['j', 'j', 'j', 'l', 'k', 'j'], "OHM-TUI v1.0"),
            (['j', 'j', 'j', 'j', 'l', 'k', 'j'], "Ayuda / Atajos"),
            ]
@pytest.mark.parametrize("secuencia_entrada, index_menu", data_nav)
def test_navegar(secuencia_entrada, index_menu):
    assert navegar(secuencia_entrada) == index_menu

data_calculo_parametro = [(['l'], 1.2, 2, 2.4),
                          (['l'], 0, 5, 0),
                          (['l'], 5, 0, 0),
                          (['l'], -5, 1, 5),
                          (['l'], 3.3, -1, 3.3),
                          (['l'], 1.2, 2, 2.4),
                          (['j', 'l'], 1.2, 2, 0.6),
                          (['j', 'l'], 0, 0, "ERR"),
                          (['j', 'l'], 1, 0, "ERR"),
                          (['j', 'l'], 0, 1, 0),
                          (['j', 'l'], 0, 0.99999, 0),
                          (['j', 'j', 'l'], 0, 0, "ERR"),
                          (['j', 'j', 'l'], 1, 0, "ERR"),
                          (['j', 'j', 'l'], 0, 1, 0),
                          (['j', 'j', 'l'], 0, 0.99999, 0),
                          ]
@pytest.mark.parametrize("secuencia_entrada, valor1, valor2, resultado", data_calculo_parametro)
def test_calcular_parametro(secuencia_entrada, valor1, valor2, resultado):
    assert calcular_parametro(secuencia_entrada, valor1, valor2) == resultado

data_normalizar_parametro = [
        #CALCULO VOLTAJE
        (['l'], "voltaje", 0.0000001, "100.00 nV"),
        (['l'], "voltaje", 5.2546, "5.25 V"),
        (['l'], "voltaje", 152340000, "152.34 MV"),

        (['l'], "corriente", 0.00000432, "4.32 uA"),
        (['l'], "corriente", 0.0142, "14.20 mA"),
        (['l'], "corriente", 123002314, "123.00 MA"),
         
        (['l'], "resistencia", 0.432, "432.00 mΩ"),
        (['l'], "resistencia", 333.34, "333.34 Ω"),
        (['l'], "resistencia", 453200134, "453.20 MΩ"),

        #CALCULO CORRIENTE
        (['j', 'l'], "corriente", 0.000000573, "573.00 nA"),
        (['j', 'l'], "corriente", 4.367, "4.37 A"),
        (['j', 'l'], "corriente", 48767004, "48.77 MA"),

        (['j', 'l'], "resistencia", 0.000000573, "573.00 nΩ"),
        (['j', 'l'], "resistencia", 220.578, "220.58 Ω"),
        (['j', 'l'], "resistencia", 12345000, "12.35 MΩ"),

        (['j', 'l'], "voltaje", 0.000015798, "15.80 uV"),
        (['j', 'l'], "voltaje", 12.688, "12.69 V"),
        (['j', 'l'], "voltaje", 15234760000, "15.23 GV"),
        #CALCULO RESISTENCIA
        (['j', 'j', 'l'], "resistencia", 0.000000573, "573.00 nΩ"),
        (['j', 'j', 'l'], "resistencia", 1.0458, "1.05 Ω"),
        (['j', 'j', 'l'], "resistencia", 20067835, "20.07 MΩ"),

        (['j', 'j', 'l'], "voltaje", 0.000015798, "15.80 uV"),
        (['j', 'j', 'l'], "voltaje", 12.688, "12.69 V"),
        (['j', 'j', 'l'], "voltaje", 15234760000, "15.23 GV"),
        
        (['j', 'j', 'l'], "corriente", 0.000000573, "573.00 nA"),
        (['j', 'j', 'l'], "corriente", 4.367, "4.37 A"),
        (['j', 'j', 'l'], "corriente", 48767004, "48.77 MA"),

        #LÍMITES SI
        (['l'], "voltaje", 1e33, "ERR"),
        (['l'], "voltaje", 1e-33, "ERR"),

        (['j', 'l'], "corriente", 1e33, "ERR"),
        (['j', 'l'], "corriente", 1e-33, "ERR"),
        
        (['j', 'j', 'l'], "resistencia", 1e33, "ERR"),
        (['j', 'j', 'l'], "resistencia", 1e-33, "ERR"),
        ] # NORMALIZAR
@pytest.mark.parametrize("secuencia_entrada, nombre_parametro, valor, valor_normalizado", data_normalizar_parametro)
def test_normalizar_parametro(secuencia_entrada, nombre_parametro, valor, valor_normalizado):
    assert normalizar_parametro(secuencia_entrada, nombre_parametro, valor) == valor_normalizado
