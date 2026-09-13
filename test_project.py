import pytest
from project import mover_cursor, navegar, calcular_voltaje, calcular_corriente, calcular_resistencia


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
            
            (['j', 'j', 'j', 'l', 'k', 'j'], "CHANGELOG"),
            (['j', 'j', 'j', 'j', 'l', 'k', 'j'], "Ayuda / Atajos"),
            ]
@pytest.mark.parametrize("secuencia_entrada, index_menu", data_nav)
def test_navegar(secuencia_entrada, index_menu):
    assert navegar(secuencia_entrada) == index_menu


data_calculo_voltaje = [(['l'], 1.2, 2, 2.4),
                        (['l'], 0, 5, 0),
                        (['l'], 5, 0, 0),
                        (['l'], -5, 1, 5),
                        (['l'], 3.3, -1, 3.3)
                        ]
@pytest.mark.parametrize("secuencia_entrada, valor1, valor2, resultado",data_calculo_voltaje)
def test_calcular_voltaje(secuencia_entrada, valor1, valor2, resultado):
    assert calcular_voltaje(secuencia_entrada, valor1, valor2) == resultado


data_calculo_corriente = [(['j', 'l'], 1.2, 2, 0.6),
                          (['j', 'l'], 0, 0, "ERR"),
                          (['j', 'l'], 1, 0, "ERR"),
                          (['j', 'l'], 0, 1, 0),
                          (['j', 'l'], 0, 0.99999, 0),
                          ]
@pytest.mark.parametrize("secuencia_entrada, valor1, valor2, resultado",data_calculo_corriente)
def test_calcular_corriente(secuencia_entrada, valor1, valor2, resultado):
    assert calcular_corriente(secuencia_entrada, valor1, valor2) == resultado


data_calculo_resistencia = [(['j', 'j', 'l'], 1.2, 2, 0.6),
                            (['j', 'j', 'l'], 0, 0, "ERR"),
                            (['j', 'j', 'l'], 1, 0, "ERR"),
                            (['j', 'j', 'l'], 0, 1, 0),
                            (['j', 'j', 'l'], 0, 0.99999, 0),
                          ]
@pytest.mark.parametrize("secuencia_entrada, valor1, valor2, resultado",data_calculo_resistencia)
def test_calcular_resistencia(secuencia_entrada, valor1, valor2, resultado):
    assert calcular_resistencia(secuencia_entrada, valor1, valor2) == resultado
