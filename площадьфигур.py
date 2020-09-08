from math import sqrt
type = input()
pi = 3.14
if type == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print(sqrt(p*(p-a)*(p-b)*(p-c)))
elif type == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a*b)
elif type == 'круг':
    r = float(input())
    print(pi*r**2)



