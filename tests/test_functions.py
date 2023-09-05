from src.functions import load_file, created_list, output_mask
import datetime
import pytest

def test_load_file():
    assert load_file('test.json') == [{'target': 'покрыть тестами 100%', 'fakt': 'покрытие 0%', 'work': 'хорошая'}]

def test_created_list():
    list_test = load_file('test2.json')
    assert created_list(list_test) == [{'date': datetime.datetime(2019, 8, 26, 10, 50, 58, 294041), 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589', 'amount': '31957.58', 'currency': 'руб.', 'state': 'EXECUTED'}]

def test_output_mask():
    assert output_mask('Счет 64686473678894779589') == 'Счет **9589'
    assert output_mask('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'