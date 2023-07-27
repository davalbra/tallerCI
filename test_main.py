import unittest
from unittest import mock
import pytest
from unittest.mock import patch,call
from main import run_order_system,compute_order_cost,show_menu,validate_order,finalize_order,check_quantity,request_user_input,food_options,max_items_per_order


def test_compute_order_cost_under_5_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 3, "2": 1}  
    assert compute_order_cost(order, food_options) == 20

def test_compute_order_cost_over_5_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 4, "2": 2}  
    assert compute_order_cost(order, food_options) == 30

def test_compute_order_cost_over_10_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 6, "2": 5}  
    assert compute_order_cost(order, food_options) == 45

def test_compute_order_cost_special_meal():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
        "3": {"name": "Chef's Special", "type": "Chef's Specials", "price": 10}
    }
    order = {"1": 3, "3": 2}  
    assert compute_order_cost(order, food_options) == 36.0  

def test_compute_order_cost_total_over_50():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 10},
        "2": {"name": "Sushi", "type": "Japanese", "price": 15},
    }
    order = {"1": 3, "2": 4}  
    assert compute_order_cost(order, food_options) == 80

def test_compute_order_cost_total_over_100():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 15},
        "2": {"name": "Sushi", "type": "Japanese", "price": 20},
    }
    order = {"1": 4, "2": 5}  
    assert compute_order_cost(order, food_options) == 125


#second part

@patch('builtins.print')
@patch('builtins.input', side_effect=['done', 'done'])
def test_run_order_system_exit_early(mock_input, mock_print):
    run_order_system()  # Añade esta línea para llamar a la función que estás probando.
    print(f'input() was called {mock_input.call_count} times')  # Debugging line
    assert mock_input.call_count == 2
    mock_print.assert_called()




@patch('builtins.print')
@patch('builtins.input', side_effect=['1', '50', 'done', 'n'])
def test_run_order_system_exceed_max_items(mock_input, mock_print):
    assert run_order_system() == -1
    assert mock_input.call_count == 4
    mock_print.assert_called()

@patch('builtins.print')
@patch('builtins.input', side_effect=['5', '2', 'done'])
def test_run_order_system_invalid_food_option(mock_input, mock_print):
    assert run_order_system() == -1
    assert mock_input.call_count == 3
    mock_print.assert_called()

@patch('builtins.print')
@patch('builtins.input', side_effect=['1', 'a', '1', '2', 'done', 'n'])
def test_run_order_system_invalid_quantity(mock_input, mock_print):
    assert run_order_system() == -1
    assert mock_input.call_count == 6
    mock_print.assert_called()

@patch('builtins.print')
@patch('builtins.input', side_effect=['1', '2', 'done', 'n'])
def test_run_order_system_cancel_order(mock_input, mock_print):
    assert run_order_system() == -1
    assert mock_input.call_count == 4
    mock_print.assert_called()

@patch('builtins.print')
@patch('builtins.input', side_effect=['1', '2', 'done', 's'])
def test_run_order_system_complete_order(mock_input, mock_print):
    assert run_order_system() == 16
    assert mock_input.call_count == 4
    mock_print.assert_called()


#show_menu
def test_show_menu():
    with patch('builtins.print') as mock_print:
        show_menu()
        calls = [call("Menu:")] + [call(f"{key}. {value['name']} ({value['type']}): ${value['price']}") for key, value in food_options.items()]
        mock_print.assert_has_calls(calls)

@patch('builtins.input', side_effect=['test_input'])
def test_request_user_input(mock_input):
    assert request_user_input('message') == 'test_input'

@pytest.mark.parametrize("amount, expected", [('5', 5), ('0', None), ('-5', None), ('a', None)])
def test_check_quantity(amount, expected):
    assert check_quantity(amount) == expected

def test_compute_order_cost():
    order = {'1': 2, '2': 3}
    assert compute_order_cost(order, food_options) == 46

def test_validate_order():
    valid_order = {'1': 2, '2': 3}
    invalid_order_food = {'4': 2}
    invalid_order_quantity = {'1': -1}  # Cambiado a -1 para representar una cantidad inválida

    assert validate_order(valid_order) == True
    assert validate_order(invalid_order_food) == False
    assert validate_order(invalid_order_quantity) == True


@patch('main.request_user_input', side_effect=['s'])
@patch('builtins.print')
def test_finalize_order(mock_print, mock_input):
    order = {'1': 2, '2': 3}
    total_price = 46
    assert finalize_order(order, total_price) == total_price

