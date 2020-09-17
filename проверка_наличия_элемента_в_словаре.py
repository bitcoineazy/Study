def is_anyone_in(collection, city):
    if city in collection.values():  # если есть среди значений словаря collection
        for name in collection.keys():  # переберите все ключи словаря
            if collection[name] == city:  # если соответствующее ключу значение равно city
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')

friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')