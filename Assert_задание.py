from typing import List, Union


def series_sum(incoming: List[Union[float, str]]) -> str:
    """Конкатенирует все элементы списка, приводя их к строкам."""
    result = ''
    for i in incoming:
        result += str(i)
    return result


mixed_numbers =[1,1.2]   # Список из int и float
result_numbers =series_sum(mixed_numbers)  # Что должна вернуть series_sum
assert series_sum([1,1.2]) == '11.2', (
    'Функция series_sum() не работает со списком чисел'
)

mixed_numbers_strings = [1,'sad'] # Cписок из чисел и строк
result_numbers_strings = series_sum(mixed_numbers_strings) # Что должна вернуть series_sum
assert series_sum([1,'sad']) == '1sad', (
    'Функция series_sum() не работает со смешанным списком'
)

empty = [] # Пустой список
result_empty = series_sum(empty)# что должна вернуть series_sum
assert series_sum([]) == '', (
    'Функция series_sum() не работает с пустым списком'
)