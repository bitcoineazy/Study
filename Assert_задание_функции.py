from typing import List, Union


def series_sum(incoming: List[Union[float, str]]) -> str:
    """Конкатенирует все элементы списка, приводя их к строкам."""
    result = ''
    for i in incoming:
        result += str(i)
    return result


mixed_numbers = [1,2.1]  # Список из int и float
result_numbers = str(12.1)
assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() не работает со списком чисел'
)

mixed_numbers_strings = [1,'sss'] # Cписок из чисел и строк
result_numbers_strings = str('1sss') # Что должна вернуть series_sum
assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() не работает со смешанным списком'
)

empty = [] # Пустой список
result_empty = ''# что должна вернуть series_sum
assert series_sum(empty) == result_empty, (
    'Функция series_sum() не работает с пустым списком'
)