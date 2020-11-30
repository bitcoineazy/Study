import unittest


class Calculator:
    """Производит различные арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Делить на ноль нельзя.')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""
    @classmethod
    def setUpClass(cls):
        """Вызывается однажды перед запуском всех тестов класса."""
        # Arrange - подготавливаем данные для теста
        cls.calc = Calculator()

    def test_divider(self):
        act = TestCalc.calc.divider(2, 1)  # вызовите метод divider с аргументом
        self.assertEqual(act, 2, 'Метод test_divider работает неправильно')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        with self.assertRaises(ZeroDivisionError):
            TestCalc.calc.divider(1, 0)
