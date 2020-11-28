from typing import Dict


def movie_quotes(name: str) -> str:
    """Возвращает цитаты известных персонажей из фильмов."""
    quotes: Dict[str, str] = {
        'Элли': 'Тото , у меня такое ощущение, что мы не в Канзасе!',
        'Шерлок': 'Элементарно, Ватсон!',
        'Дарт Вейдер': 'Я — твой отец.',
        'Thomas A. Anderson': 'Меня. Зовут. Нео',
        'Алиса Плезенс Лидделл': 'Всё чудесатее и чудесатее!',
    }
    return quotes.get(name, 'Персонаж пока не известен миллионам.')

# Утверждаем, что если в movie_quotes передать 'Шерлок' -
# функция вернёт 'Элементарно, Ватсон!'.
assert movie_quotes('Шерлок') == 'Элементарно, Ватсон!', (
   "movie_quotes('Шерлок') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes передать 'Thomas A. Anderson' -
# функция вернёт 'Меня зовут Нео!'.
assert movie_quotes('Thomas A. Anderson') == 'Меня. Зовут. Нео', (
    "movie_quotes('Thomas A. Anderson') не вернул ожидаемый результат!")

# Утверждаем, что если в movie_quotes передать 'Алиса Плезенс Лидделл' -
# функция вернёт 'Всё чудесатее и чудесатее!'.
expected_answer = 'Всё чудесатее и чудесатее!'
assert movie_quotes('Алиса Плезенс Лидделл') == expected_answer, (
    "movie_quotes('Алиса Плезенс Лидделл') не вернул ожидаемый результат!")


class Contact:
    name: str
    year_birth: int
    is_programmer: bool

    def __init__(self,
                 name: str,
                 year_birth: int,
                 is_programmer: bool) -> None:
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self) -> str:
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        elif self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return(f'{self.name}, '               
               f'категория: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self) -> None:
        print(self.show_contact())

mike: Contact = Contact('Михаил Булгаков', 1891, False)

expected_string: str = ('Михаил Булгаков, категория: Старейшина, статус: Нормальный')

assert mike.show_contact() == expected_string, "Ошибка в Contact.show_contact()"

'''За кулисами assert
При обработке инструкций assert Python преобразовывает каждую из них примерно в такую конструкцию:
if __debug__:
    if not <утверждение>:
        raise AssertionError(<сообщение об ошибке>) '''