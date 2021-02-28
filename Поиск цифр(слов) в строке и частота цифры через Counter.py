'''Реализуйте функцию, для поиска в строке цифр,
 представленных в виде цифр или слов, для встречи
 которых в любом виде составляется словарь, ключами
  которого являются все цифры, а значениями число упоминаний
   о них в строке в любом виде. Проверить работу функции при произвольных параметрах.'''
import re
from collections import Counter


str1 = '1 2 3 2 1 3 one two three four'
def func(str1):
    num = []
    num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    for i in str1:
        if i.isdigit():
            num.append(i)
    pattern = re.findall('\w+', str1)
    print(pattern)
    for each in pattern:
        if each in num_dict.keys():
            num.append(str(num_dict[each]))
    output = ''.join(num)
    c = Counter(zip(output))
    print(c)

func(str1)
'''str1 = 'bjib2342b4ob1jkb12j4bjb32j42jbjb'
dic = {}
for i in str1:
    if i.isdigit():
        dic[i] = dic[i].get(i, 0) + 1
print(dic)'''