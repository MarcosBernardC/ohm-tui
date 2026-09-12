import pytest
from project import mover_cursor


data_mover_cursor = [
        (['k'], (1, 1)),
        (['k', 'j'], (2, 1)),
        (['k', 'j', 'j'], (3, 1)),
        (['k', 'j', 'j', 'j'], (4, 1)),
        (['k', 'j', 'j', 'j', 'j'], (5, 1)),
        (['k', 'j', 'j', 'j', 'j', 'j', 'j'], (5, 1))]

@pytest.mark.parametrize("secuencia_de_movimiento, posicion_cursor", data_mover_cursor)
def test_mover_cursor(secuencia_de_movimiento, posicion_cursor):
    posicion_final = mover_cursor(secuencia_de_movimiento)

    assert posicion_final == posicion_cursor

     
def test_req_func_2():
    pass

def test_req_func_3():
    pass
