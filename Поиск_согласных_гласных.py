str1 = 'asdxzczxaaaaaaaaa'
str2 = 'adsszxxzcxzc'
key = 'C'
def func(str1, str2, key):
    if key == 'C':
        vowels_1 = 0
        consonants_1 = 0
        vowels_2 = 0
        consonants_2 = 0
        for i in str1:
            letter = i.lower()
            if letter == "a" or letter == "e" or \
                    letter == "i" or letter == "o" or \
                    letter == "u" or letter == "y":
                vowels_1 += 1
            else:
                consonants_1 += 1
        for i in str2:
            letter = i.lower()
            if letter == "a" or letter == "e" or \
                    letter == "i" or letter == "o" or \
                    letter == "u" or letter == "y":
                vowels_2 += 1
            else:
                consonants_2 += 1
        if consonants_1 > consonants_2:
            print('в строке 1 больше согл, чем в строке 2')
        else:
            print('в строке 2 больше согл, чем в строке 2')
    if key == 'a-z':
        if len(str1) > len(str2):
            print('в строке 1 больше букв, чем в строке 2')
        else:
            print('в строке 2 больше букв, чем в строке 1')

func(str1, str2, key)