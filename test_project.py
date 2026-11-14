import pytest
from decimal import Decimal

from project import mover_cursor, navegar, calcular_parametro, normalizar_parametro

from src.models.ohm_model import OhmModel, Corriente, Voltaje, Resistencia


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
            (['l', 'k', 'j', 'j'], "1.3."),
            (['l', 'k', 'j', 'j', 'j'], "1.3."),
            (['l', 'k', 'j'], "1.2."),
            (['j', 'l', 'k'], "2.1."),  # CURRENT MENU
            (['j', 'l', 'k', 'j'], "2.2."),
            (['j', 'l', 'k', 'j', 'j'], "2.3."),
            (['j', 'l', 'k', 'j', 'j', 'j'], "2.3."),
            (['j', 'j', 'l', 'k'], "3.1."),  # RESISTANCE MENU
            (['j', 'j', 'l', 'k'], "3.1."),
            (['j', 'j', 'l', 'k', 'j'], "3.2."),
            (['j', 'j', 'l', 'k', 'j', 'j'], "3.3."),
            (['j', 'j', 'l', 'k', 'j', 'j', 'j'], "3.3."), 
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
        (['l'], "voltaje", Decimal("0.0000001"), (Decimal('100.00'), 'n')),
        (['l'], "voltaje", Decimal("5.2546"), (Decimal('5.25'), '')),
        (['l'], "voltaje", Decimal("152340000"), (Decimal('152.34'), 'M')),

        (['l'], "corriente", Decimal("0.00000432"), (Decimal('4.32'), 'u')),
        (['l'], "corriente", Decimal("0.0142"), (Decimal('14.20'), 'm')),
        (['l'], "corriente", Decimal("123002314"), (Decimal('123.00'), 'M')),

        (['l'], "resistencia", Decimal("0.432"), (Decimal('432.00'), 'm')),
        (['l'], "resistencia", Decimal("333.34"), (Decimal('333.34'), '')),
        (['l'], "resistencia", Decimal("453200134"), (Decimal('453.20'), 'M')),
        #
        # #CALCULO CORRIENTE
        (['j', 'l'], "corriente", Decimal("0.000000573"), (Decimal('573.00'), 'n')),
        (['j', 'l'], "corriente", Decimal("4.367"), (Decimal('4.37'), '')),
        (['j', 'l'], "corriente", Decimal("48767004"), (Decimal('48.77'), 'M')),

        (['j', 'l'], "resistencia", Decimal("0.000000573"), (Decimal('573.00'), 'n')),
        (['j', 'l'], "resistencia", Decimal("220.578"), (Decimal('220.58'), '')),
        (['j', 'l'], "resistencia", Decimal("12345000"), (Decimal('12.34'), 'M')),

        (['j', 'l'], "voltaje", Decimal("0.000015798"), (Decimal('15.80'), 'u')),
        (['j', 'l'], "voltaje", Decimal("12.688"), (Decimal('12.69'), '')),
        (['j', 'l'], "voltaje", Decimal("15234760000"), (Decimal('15.23'), 'G')),
        #CALCULO RESISTENCIA
        (['j', 'j', 'l'], "resistencia", Decimal("0.000000573"), (Decimal('573.00'), 'n')),
        (['j', 'j', 'l'], "resistencia", Decimal("1.0458"), (Decimal('1.05'), '')),
        (['j', 'j', 'l'], "resistencia", Decimal("20067835"), (Decimal('20.07'), 'M')),

        (['j', 'j', 'l'], "voltaje", Decimal("0.000015798"), (Decimal('15.80'), 'u')),
        (['j', 'j', 'l'], "voltaje", Decimal("12.688"), (Decimal('12.69'), '')),
        (['j', 'j', 'l'], "voltaje", Decimal("15234760000"), (Decimal('15.23'), 'G')),

        (['j', 'j', 'l'], "corriente", Decimal("0.000000573"), (Decimal('573.00'), 'n')),
        (['j', 'j', 'l'], "corriente", Decimal("4.367"), (Decimal('4.37'), '')),
        (['j', 'j', 'l'], "corriente", Decimal("48767004"), (Decimal('48.77'), 'M')),

        #LÍMITES SI
        (['l'], "voltaje", Decimal("1e33"), ('ERR', '')),
        (['l'], "voltaje", Decimal("1e-33"), ('ERR', '')),

        (['j', 'l'], "corriente", Decimal("1e33"), ('ERR', '')),
        (['j', 'l'], "corriente", Decimal("1e-33"), ('ERR', '')),

        (['j', 'j', 'l'], "resistencia", Decimal("1e33"), ('ERR', '')),
        (['j', 'j', 'l'], "resistencia", Decimal("1e-33"), ('ERR', '')),
        #LÍMITES 999.999
        (['l'], "voltaje", Decimal("999.999"), (Decimal('1.00'), 'k')),
        (['j', 'l'], "corriente", Decimal("999.999"), (Decimal('1.00'), 'k')),
        (['j', 'j', 'l'], "resistencia", Decimal("999.999"), (Decimal('1.00'), 'k')),
        ] # NORMALIZAR
@pytest.mark.parametrize("secuencia_entrada, nombre_parametro, valor, valor_normalizado", data_normalizar_parametro)
def test_normalizar_parametro(secuencia_entrada, nombre_parametro, valor, valor_normalizado):
    assert normalizar_parametro(secuencia_entrada, nombre_parametro, valor) == valor_normalizado

# def test_calcular(unidad_a_calcular, valor1, valor2, resultado):
def test_calcular():
    unidad_a_calcular = 'V'
    ohm_model = OhmModel()
    ohm_model.corriente = Corriente(valor=Decimal("1.50"))
    ohm_model.resistencia = Resistencia(valor=Decimal("2.00"))
    ohm_model.calcular(unidad_a_calcular)
    assert ohm_model.voltaje.valor == Decimal("3.00")

