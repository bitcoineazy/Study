import time


def partition_by_tasks(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if array[i] >= array[start]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def partition_by_penalty(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if array[i][2] <= array[start][2]:
            #print('zz')
            if array[i][1] == array[start][1]:
                #print('jj')
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def partition_by_names(array, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if array[i][2] == array[start][2] and array[i][1] == array[start][1]:
            if array[i][0] < array[start][0]:
                #print('jaja')
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot


def eff_quick_sort(array, start, end):
    def sort_tasks_amount(array, start, end):
        if start > end:
            return
        pivot = partition_by_tasks(array, start, end)
        eff_quick_sort(array, start, pivot - 1)
        eff_quick_sort(array, pivot + 1, end)

    def sort_penalty(array, start, end):
        if start > end:
            return
        pivot_penalty = partition_by_penalty(array, start, end)
        eff_quick_sort(array, start, pivot_penalty - 1)
        eff_quick_sort(array, pivot_penalty + 1, end)

    def sort_names(array, start, end):
        if start > end:
            return
        pivot_names = partition_by_names(array, start, end)
        eff_quick_sort(array, start, pivot_names - 1)
        eff_quick_sort(array, pivot_names + 1, end)

    return sort_tasks_amount(array, start, end)#, sort_penalty(array, start, end), sort_names(array, start, end)


if __name__ == '__main__':
    #time_start = time.time()
    #n = int(input())
    n = 6
    #info_z = [input().split(' ') for i in range(n)]
    #info_z = [['tufhdbi', '76', '58'], ['rqyoazgbmv', '59', '78'], ['qvgtrlkmyrm', '35', '27'], ['tgcytmfpj', '70', '27'],
     #        ['xvf', '84', '19'], ['jzpnpgpcqbsmczrgvsu', '30', '3'], ['evjphqnevjqakze', '92', '15'], ['wwzwv', '87', '8'],
    #         ['tfpiqpwmkkduhcupp', '1', '82'], ['tzamkyqadmybky', '5', '81'], ['amotrxgba', '0', '6'], ['easfsifbzkfezn', '100', '28'],
    #        ['easfsifbzkfezn', '100', '28'], ['easfsifbzkfezn', '100', '28'],
    #         ['Просто', 'тест']]
    info = [None] * n
    for i in range(n):
        info[i] = [int(info_z[i][1]), int(info_z[i][2]), info_z[i][0]]
    #print(info, 'info')
    '''for each in info:
        if len(each) == 3:
            each[0] = int(each[1])
            each[1] = int(each[2])
            each[2] = each[0]
        else:
            info.pop()'''
    #print(info)
    eff_quick_sort(info, start=0, end=n - 1)
    #print(*map(lambda x: x[2], info))
    for i in range(n):
        print(info[i][2])
    #print(time.time() - time_start)
