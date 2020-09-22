DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_friends(friends_count):
    if friends_count == 1:
        return 'У тебя 1 друг'
    elif 2 <= friends_count <= 4:
        return 'У тебя ' + str(friends_count) + ' друга'
    elif friends_count >= 5:
        return 'У тебя ' + str(friends_count) + ' друзей'


def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return format_friends(count)
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        city_values = set(DATABASE.values())
        return  'Твои друзья в городах: ' + ', '.join(city_values)
    else:
        return '<неизвестный запрос>'


def runner():
    print('Привет, я Анфиса!')
    print(process_query('Сколько у меня друзей?'))
    print(process_query('Кто все мои друзья?'))
    print(process_query('Где все мои друзья?'))

runner()
