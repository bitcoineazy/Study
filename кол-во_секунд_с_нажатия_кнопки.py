'''Задание 9. Разработать программу измерения простой двигательной реакции.
В течение минуты через случайные промежутки времени производится звуковой сигнал,
испытуемый должен как можно быстрее нажать на кнопку по этому сигналу.
Фиксируется время реакции в миллисекундах - разность времени сигнала и времени
нажатия на клавишу компьютера. Результаты теста записать в отдельный файл,
где фиксируются - Имя, Фамилия, дата проведения испытания, результат теста.
 Построить график изменения скорости реакции по нескольким попыткам по данным из файла результатов.¶'''
import winsound
import keyboard
import matplotlib.pyplot as plt
import time
import random
import csv


frequency = {}
array = []
array_time_pass = []
time_start = time.time()



while time.time() - time_start < 5:

    time.sleep(random.randint(1,2))
    winsound.Beep(500, 100)
    time_beep = time.time()
    array.append(keyboard.read_key())
    array_time_pass.append(time.time() - time_beep)



print(array)
for i in range(len(array)):
    frequency.update({array[i]:array_time_pass[i]})

print(frequency)
plt.plot(array,array_time_pass)
plt.xlabel('Кнопка', color='red')
plt.ylabel('Скорость реакции', color='blue')
plt.title('Скорость реакции на звук')
plt.show()
name = input('Введите имя')
with open(r'C:\Users\79268\Dev\csvs'+f"\\{name}.csv", mode='w', newline='') as f:

    fieldnames = array
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(frequency)