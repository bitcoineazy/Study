#Реализовать функцию factorial(n) двумя способами: с помощью цикла и рекурсии

'''def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    print(fact)

'''
'''def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)'''

'''1.2) Реализовать функции printIn(s) и printOut(s),
 которые выводят строки s с отступами, при этом каждый вывод printIn(s)
  приводит к увеличению отсутпа, а каждый вывод printOut(s) приводит к уменьшению отсутпа.'''

def printIn(s):
    global deep

    fact = 1
    for num in range(2, n + 1):
        fact *= num
    #print(fact)

def factorial(n):
    global x
    fact = 1
    k = 0
    x = n
    sp_amount = 0

    for num in range(2, n + 3):
        fact *= num
        k += 1
        print(f'{"    " *k}factorial({x})')
        x -= 1
        sp_amount += 4

    fact = 1
    print(f'{" "*sp_amount}{fact}')
    for reversed in range(1, n + 1):
        fact *= reversed
        print(f'{" "*(sp_amount-k)} {fact}')
        x += 1
        k += 4


#factorial(4)

def fib(n):
    global x
    x = 0
    if n < 2:
        return n

    x += 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i+1))
print(x)