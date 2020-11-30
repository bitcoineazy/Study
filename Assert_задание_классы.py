class Contact:
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
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self) -> None:
        print(self.show_contact())

user1 = Contact('Mike Bulgakov', 1891, False)
'''den = Contact('Den', 1891, True)'''
expected_string: str = 'Mike Bulgakov, возраст: Старейшина, статус: Нормальный'
age_string: str = 'Старейшина'
assert user1.age_define() == age_string, (
   'Ошибка в Contact.age_define()')
user2 = Contact('Nike', 1990, False)
#print(user1.age_define())
expected_string_2: str = 'Nike, возраст: Молодой, статус: Нормальный'
age_string_2: str = 'Молодой'
assert user2.age_define() == age_string_2, (
   'Ошибка в Contact.age_define()')
user3 = Contact('Max', 1950, False)
age_string_3: str = 'Олдскул'
assert user3.age_define() == age_string_3, (
    'Ошибка в Contact.age_define()'
)
user4 = Contact('Mike Bulgakov', 1891, False)
expected_string_4: str = 'Mike Bulgakov, возраст: Старейшина, статус: Нормальный'
programmer_string: str = 'Нормальный'
assert user4.programmer_define() == programmer_string,(
    'Ошибка в Contact.programmer_define()')
user5 = Contact('Mike Bulgakov', 1891, True)
programmer_string_2: str = 'Программист'
assert user5.programmer_define() == programmer_string_2,(
    'Ошибка в Contact.programmer_define()'
)
user5 = Contact('Гвидо ван Россум', 1956, True)
user5.print_contact()
