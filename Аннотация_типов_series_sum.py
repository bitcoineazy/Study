from typing import List, Union

def series_sum(incoming: List[Union[str, float]]) -> str:
    """Принимает на вход список, приводит его элементы к строкам
    и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result

print(series_sum.__annotations__)