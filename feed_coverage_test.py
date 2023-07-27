import io
import sys
import unittest
import main  # asumamos que este es tu archivo principal
from unittest import mock
from contextlib import redirect_stdout
def test_show_menu(capsys):  # capsys es una función especial de pytest que captura la salida de print()
    expected_output = """Menu:
1. Spaghetti (Italian): $8
2. Sushi (Japanese): $10
3. Tacos (Mexican): $6
4. Tacos (Chef's Specials): $20
"""  # ajusta esto según la salida esperada
    main.show_menu()
    captured = capsys.readouterr()  # lee la salida de print()
    assert captured.out == expected_output  # asegura que la salida es igual a la esperada


def test_request_user_input():
    with mock.patch('builtins.input', return_value='test'):
        assert main.request_user_input('Ingrese algo: ') == 'test'

def test_check_quantity():
    # Caso con una cantidad válida
    assert main.check_quantity('3') == 3

    # Caso con una cantidad no válida (menor o igual a 0)
    assert main.check_quantity('-2') == None
    assert main.check_quantity('0') == None

    # Caso con una cantidad que no puede convertirse en entero
    assert main.check_quantity('abc') == None
    assert main.check_quantity('') == None


def test_compute_order_cost():
    # Pedido sin descuentos
    order = {"1": 1, "2": 1}
    assert main.compute_order_cost(order, main.food_options) == 18  

    # Pedido con descuentos
    order = {"1": 5, "2": 5}
    assert main.compute_order_cost(order, main.food_options) == 62  

    # Pedido con descuentos especiales
    order = {"1": 10, "2": 10}
    assert main.compute_order_cost(order, main.food_options) == 109 

    # Pedido con recargo para comidas especiales
    order = {"1": 1, "4": 1}
    assert main.compute_order_cost(order, main.food_options) == 29  


def test_validate_order():
    # Prueba con una orden válida
    valid_order = {"1": 1, "2": 2}
    assert main.validate_order(valid_order) == True

    # Prueba con una orden inválida (contiene alimentos no presentes en el menú)
    invalid_order = {"5": 1}
    assert main.validate_order(invalid_order) == False

    # Prueba con una orden inválida (cantidad de alimentos es None)
    invalid_order_amount = {"1": None}
    assert main.validate_order(invalid_order_amount) == False

    # Prueba con una orden inválida (la cantidad total de alimentos excede el límite)
    exceeding_order = {"1": 101, "2": 2}
    assert main.validate_order(exceeding_order) == False
import unittest.mock

@unittest.mock.patch('builtins.input', return_value='s')
def test_finalize_order_confirm(mocked_input):
    order = {"1": 1, "2": 2}
    total_price = 20
    assert main.finalize_order(order, total_price) == total_price

@unittest.mock.patch('builtins.input', return_value='n')
def test_finalize_order_cancel(mocked_input):
    order = {"1": 1, "2": 2}
    total_price = 20
    assert main.finalize_order(order, total_price) == -1

import unittest.mock

# @unittest.mock.patch('builtins.input', side_effect=['1', '1', 'done', 's'])
# def test_run_order_system(mocked_input):
#     assert main.run_order_system() > 0

@unittest.mock.patch('builtins.input', side_effect=['1', '1asd', 'done', 's'])
def test_run_order_system(mocked_input):
    assert main.run_order_system() == 0

@unittest.mock.patch('builtins.input', side_effect=['1', '101', 'done', 's'])
def test_run_order_system_invalid_amount(mocked_input):
    assert main.run_order_system() == -1
