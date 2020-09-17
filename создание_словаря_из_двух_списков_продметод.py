friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

# допишите ваш код сюда
for keys in friends_names:
    for values in friends_cities:
        friends[keys] = values
        friends_cities.remove(values)
        break

print('Лена живет в городе', friends['Лена'])

