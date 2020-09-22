blok_string = 'Ночь. Улица. Фонарь. Аптека' 
# из строки получаем список, где строку делят по сочетанию точки и пробела:
blok_list = blok_string.split('. ')
blok_list1 = blok_string.split()
print(blok_list)
print(blok_list[-1])
for i in range (0, len(blok_list1)):
    print(blok_list1[i].strip('.'))