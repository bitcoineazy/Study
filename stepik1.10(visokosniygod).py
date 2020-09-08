Y = int(input())
if (Y % 4 == 0 and Y % 100 != 0)  :
    print('Високосный')
elif Y % 400 == 0 :
    print('Високосный')
else :
    print('Обычный')
