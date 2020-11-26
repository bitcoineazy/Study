def func(x, y):
    return x + y


print(type(func))
# результат: <class 'function'>


print(hex(id(func)))
#0x2071bd85310 -
new_func = func
print(new_func(1,2))
print(hex(id(new_func)))
#0x2071bd85310 - одинаковые
'''
Старую переменную func мы переопределили, но new_func продолжает указывать на ту же самую функцию, на которую изначально указывало имя func.
Поскольку функция ведет себя как обычная переменная, то ее можно передавать в качестве параметра в другую функцию:
'''
def apply(f, x, y):
    return f(x, y) // 2


print(apply(new_func, 1, 2))
# результат: 3//2 = 1

'''Если функцию можно передать, то что мешает вернуть функцию?'''


def operation(name):
    def add(x, y):
        return x + y

    def mul(x, y):
        return x * y

    if name == 'add':
        return add

    if name == 'mul':
        return mul


# сложение
op = operation('add')
print(op(1, 3))
# результат: 4

# умножение
op2 = operation('mul')
print(op2(2, 5))
# результат: 10

op3 = operation('mul')
print(op3(452, 123))
#результат: 55596
# или даже так: умножение, но без промежуточной функции
print(operation('mul')(2, 5))
# результат: 10

'''
Внутри функции мы создали другие функции, а потом внешним переменным присвоили ссылки на эти «внутренние» функции.
Можно сделать еще один шаг: обернуть входящую функцию нужным кодом прежде, чем её исполнить.
Создадим функцию wrapper()
Передадим ей как параметр функцию some_func()
Функция wrapper() передаёт some_func() в свою внутреннюю функцию added_value(), которая выполняет некие полезные действия
Функция wrapper() возвращает функцию added_value()
'''


def wrapper(func):
    # какие-то действия с func
    _cache = {'counter': 0}

    def added_value():
        _cache['counter'] = _cache['counter'] + 1
        print("Полезная работа до начала работы функции")
        func()
        print("Полезная работа после выполнения функции")

    return added_value


def some_func():
    print("Я полезная функция")


do = wrapper(some_func)
do()
# результат:
# Полезная работа до начала работы функции
# Я полезная функция
# Полезная работа после выполнения функции

def cache_args(func):
    cached_args = {}
    def wrapper(num):
        if num in cached_args:
            return cached_args[num]
        cached_args[num] = func(num)
        return cached_args[num]
    return wrapper

@cache_args
def long_heavy(num):
     print(f"Долго и сложно {num}")
     return num**num

print(long_heavy(1))
print(long_heavy(1))
print(long_heavy(2))
print(long_heavy(2))
print(long_heavy(2))
print(long_heavy(2))
print(long_heavy(3))
print(long_heavy(3))
'''Долго и сложно 1
1
1
Долго и сложно 2
4
4
4
4
Долго и сложно 3
27
27
'''