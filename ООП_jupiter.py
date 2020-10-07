# импортируйте библиотеку math
import math
class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = (4*math.pi*radius**2) # здесь вычислите площадь поверхности шара
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = (temp_celsius*(9/5)+32) # здесь переведите температуру в градусы Фаренгейта

    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")

jupiter = Planet('Юпитер', 69911, -108)
# вызовите метод show_info для Юпитера
jupiter.show_info()