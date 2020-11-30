from typing import Callable, List

'''Допишите тестирующую функцию test_sort(). Она должна проверять функции, сортирующие списки из чисел по возрастанию (от меньшего к большему).
Например, если на вход такая функция получит [1, 3, 2, 4], то вернуть она должна [1, 2, 3, 4]
В прекоде заготовлен вызов тестирования нескольких сортирующих функций (эти функции вам не видны).
В тесте проверьте, работают ли эти функции
со списком, содержащим int и float;
со списком, содержащим отрицательные величины, нулевое значение;
со списком, содержащим одинаковые числа;
с пустым списком (всегда стоит проверять граничные значения).
Часть функций не пройдёт все тесты.
Когда вы обнаружите неработающие функции — удалите из кода строки, где они вызываются на тестирование. После этого отправляйте код на проверку.
Каждую проверку описывайте в отдельном ассерте, задавая для тестируемой функции нужный аргумент и ожидаемый ответ.'''
# Нам не важно, что примимает на вход функция sorting_algorithm
# лишь бы она возвращала отсортированный список.
# Поэтому в аннотации типа аргумента указаны Ellipsis (...)
def test_sort(sorting_algorithm:
Callable[..., List[float]]) -> None:
    """Тестируем алгоритм, сортирующий список по возрастанию."""
    print(f'{test_sort.__doc__}')
    print(f'Тестируем функцию: {sorting_algorithm.__name__}')

    source = [4, 3.3]
    sorted = [3.3, 4]
    assert sorting_algorithm(source) == sorted, (
        f'Алгоритм в {sorting_algorithm.__name__} работает неправильно '  
        f'со строкой "{source}"'
    )
    source_2 = [0, -2]
    sorted_2 = [-2, 0]
    assert sorting_algorithm(source_2) == sorted_2, (
        f'Алгоритм в {sorting_algorithm.__name__} работает неправильно '
        f'со строкой "{source}"'
    )
    source_3 = [10, 10]
    sorted_3 = [10, 10]
    assert sorting_algorithm(sorted_3) == sorted_3, (
        f'Алгоритм в {sorting_algorithm.__name__} работает неправильно '
        f'со строкой "{source}"'
    )
    source_4 = []
    sorted_4 = []
    assert sorting_algorithm(source_4) == source_4, (
        f'Алгоритм {sorting_algorithm.__name__} работает неправильно '
        'с пустой строкой'
    )


    print(f'Тест для {sorting_algorithm.__name__} пройден')


test_sort(ttd_sprint5_data.bubble_sort)
test_sort(ttd_sprint5_data.timsort_sort)
test_sort(ttd_sprint5_data.selection_sort)
test_sort(ttd_sprint5_data.insertion_sort)
test_sort(ttd_sprint5_data.cap_sort)
test_sort(ttd_sprint5_data.merge_sort)
test_sort(ttd_sprint5_data.heap_sort)
test_sort(ttd_sprint5_data.stepa_sort)
test_sort(ttd_sprint5_data.quick_sort)
test_sort(ttd_sprint5_data.sus_sort)