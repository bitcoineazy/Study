def print_friends_count(friends_count, name=''):  #аргумент name для имени
    if friends_count == 1:
        text = '1 друг'
    elif 2 <= friends_count <= 4:
        text = str(friends_count) + ' друга'  #склонение счётчика друзей
    elif friends_count >= 5:
        text = str(friends_count) + ' друзей' #склонение счётчика друзей
    if name != '':  #начинается с if(как новое условие для аргумента name), проверка не является ли поле name пустым
        print(name+', у тебя', text)
    else: #если name является пустым, то
        print('У тебя', text)



print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')
