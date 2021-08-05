from itertools import permutations


# Самое большое число, которое
# можно составить из элементов списка
def biggest_number(n, values):
    numbers = values.split(' ')
    counter = '0'
    max_per = 0
    for i in range(n, n + 1):
        for z in permutations(numbers, i):
            for y in range(len(z)):
                counter += z[y]
            if int(counter) > max_per:
                max_per = int(counter)
            counter = ''
    print(max_per)


if __name__ == '__main__':
    # n = int(input())
    n = 5
    # numbers = input()
    numbers = '2 4 5 2 10'
    biggest_number(n, numbers)
