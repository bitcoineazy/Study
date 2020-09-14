FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']

def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


# перенесите в функцию process_query() вот этот код:
def process_query(query):
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    if query == 'Сколько у меня друзей?':
        print('У тебя',count,'друзей')
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(FRIENDS)
        print('Твои друзья:', friends_string)
    else:
        print('<неизвестный запрос>')


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')
process_query('Кто все мои друзья?')