from typing import Callable

def add(number: float, callback: Callable[[float], float]) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    >>> add(2.8, adder20)
    22.8
    >>> add(2, multiplier2)
    4
    """
    return callback(number)


def adder20(number: float) -> float:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: float) -> float:
    """Умножает аргумент на 2."""
    return number * 2
print(add.__annotations__)
print(adder20.__annotations__)
print(multiplier2.__annotations__)
