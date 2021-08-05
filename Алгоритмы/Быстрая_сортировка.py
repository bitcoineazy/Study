from random import randint


def partition(array, pivot):
    less = [i for i in array if i < pivot]  # элементы array, меньшие pivot
    center = [i for i in array if i == pivot]  # элементы array, равные pivot
    greater = [i for i in array if i > pivot]  # элементы array, большие pivot
    return less, center, greater


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[randint(0, len(array) - 1)]  # опора, случайный элемент из array
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


print(quicksort([1, 3, 98, 54, 20, 8, 10, 2]))
