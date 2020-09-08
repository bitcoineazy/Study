A = int(input())  #A - рекоменд, B - не стоит спать больше, H - сколько аня спит
B = int(input())
H = int(input())
if H > B :
    print('Пересып')
elif H < A :
    print('Недосып')
else :
    print('Это нормально')