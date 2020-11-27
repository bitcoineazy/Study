

from typing import Sequence, Tuple, List, Set, Optional, Dict




def lower_join(seq: Sequence[str]) -> str:
    """Принимает на вход последовательность и создаёт из неё
    строку в нижнем регистре."""
    return ''.join(seq).lower()

print(lower_join('sASDd'))
print(lower_join.__annotations__)
