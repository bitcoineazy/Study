# Создайте исключение здесь
class NameLengthException(Exception):
    pass

name = 'ЛилуминАй ЛекатАриба ЛаминачАй Экбат Дэ СэбАт'


def check_name(name):
    if len(name) > 4:
        raise NameLengthException('Длина больше 4-х символов')


# Закомментируйте или удалите код ниже, когда будете отправлять решение на проверку
check_name(name)

