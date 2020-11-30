import unittest

'''Методика TDD подразумевает, что сначала пишутся тесты, а потом код.'''
'''В коде задания описан метод summ.
Если вызвать этот метод без аргументов, он вернёт ноль, а если передать в метод summ один аргумент — он вернёт значение этого аргумента.
Это не лучшее поведение для калькулятора, надо его изменить. Методика TDD подразумевает, что сначала пишутся тесты, а потом код.
В этом задании напишите тесты, которые проверяют, что summ возвращает None, если количество переданных аргументов меньше двух.'''
class Calculator:
    def summ(self, *args):
        """Возвращает сумму принятых аргументов."""
        sum = 0
        if len(args) <= 1: #проверка кол-ва подаваемых аргументов
            return None
        for i in args:
            sum += i
        return sum


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""
    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = TestCalc.calc.summ(3, -3, 5)
        self.assertEqual(act, 5, 'summ работает неправильно')

    '''В Unittest есть встроенный метод для проверки на None: assertIsNone(x)
Маленькие тесты — это всегда хорошо. Одна проверка — один тест:
test_summ_no_argument — что будет, если функция вызвана без аргументов
test_summ_one_argument — что будет, если функция вызвана с одним аргументом.'''

    def test_summ_no_argument(self):
        act = TestCalc.calc.summ()
        self.assertIsNone(act)

    def test_summ_one_argument(self):
        act = TestCalc.calc.summ(1)
        self.assertIsNone(act)