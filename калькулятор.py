fir = float(input())
sec = float(input())
oper = input()

if oper == '+':
    print(fir+sec)
elif oper == '-':
    print(fir-sec)
elif oper == '/' and sec != 0:
    print(fir/sec)
elif oper == '/' and sec == 0:
    print('Деление на 0!')
elif oper == '*':
    print(fir*sec)
elif oper == 'mod' and sec != 0:
    print(fir%sec)
elif oper == 'mod' and sec == 0:
    print('Деление на 0!')
elif oper == 'pow':
    print(fir**sec)
elif oper == 'div' and sec != 0:
    print(fir//sec)
elif oper == 'div' and sec == 0:
    print('Деление на 0!')


