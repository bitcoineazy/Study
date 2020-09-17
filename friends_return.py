FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def show_count_friends(count_friends):
    if count_friends == 1:
        return ('У тебя 1 друг')
    elif 2 <= count_friends <= 4:
        return ('У тебя ' + str(count_friends) + ' друга')
    elif count_friends >= 5:
        return ('У тебя ' + str(count_friends) + ' друзей')


def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(FRIENDS)
        return show_count_friends(count)
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(FRIENDS)
        return('Твои друзья: '+friends_string)
    else:
        return str('<неизвестный запрос>')


# Внимание! Это те самые вызовы, которые не надо трогать
print(process_query('Сколько у меня друзей?'))
print(process_query('Кто все мои друзья?'))
print(process_query('Как меня зовут?'))