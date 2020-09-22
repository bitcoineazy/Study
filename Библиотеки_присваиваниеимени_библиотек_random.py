# здесь подключите библиотеку random и дайте ей краткое имя
import random as r

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']


def how_are_you():
    return r.choice(answers)
    # напишите ваш код здесь


print(how_are_you())
