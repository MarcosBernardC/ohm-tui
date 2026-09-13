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


def test_calcular_voltaje():
    assert calcular_voltaje(['l'], 1.2, 2) == 2.4
 
def test_calcular_corriente():
    assert calcular_corriente(['j', 'l'], 1.2, 2) == 0.6

def test_calcular_resistencia():
    assert calcular_resistencia(['j', 'j', 'l'], 1.2, 2) == 0.6
