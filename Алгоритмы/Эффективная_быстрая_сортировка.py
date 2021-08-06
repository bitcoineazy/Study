def partition(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if array[i] <= array[start]:
            array[i], array[pivot + 1] = array[pivot + 1], array[i]
            pivot += 1
    array[start], array[pivot] = array[pivot], array[start]
    return pivot


def solution(array, start, end):
    def quick_sort(array, start, end):
        if start > end:
            return
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)

    return quick_sort(array, start, end)


def main():
    #n = int(input())
    #data = [input() for i in range(n)]
    n = 16
    data = [['tufhdbi', '76', '58'], ['rqyoazgbmv', '59', '78'], ['qvgtrlkmyrm', '35', '27'],
            ['tgcytmfpj', '70', '27'],
            ['xvf', '84', '19'], ['jzpnpgpcqbsmczrgvsu', '30', '3'], ['evjphqnevjqakze', '92', '15'],
            ['wwzwv', '87', '8'],
            ['tfpiqpwmkkduhcupp', '1', '82'], ['tzamkyqadmybky', '5', '81'], ['amotrxgba', '0', '6'],
            ['easfsifbzkfezn', '100', '28'],
            ['kivdiy', '70', '47'], ['audi', '70', '47'], ['gosha', '80', '47'], ['rita', '80', '47']]
    for i in range(n):
        data[i] = [-int(data[i][1]), int(data[i][2]), data[i][0]]
    solution(data, start=0, end=n - 1)
    answer = map(lambda x: x[2], data)
    print('\n'.join(answer))


if __name__ == '__main__':
    main()
