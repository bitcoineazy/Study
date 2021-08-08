# Функция должна вернуть индекс элемента, равного target
# Временная сложность: O(log n)
def broken_search(nums, target) -> int:
    def index_search(array, left, right, target):
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        if right < left:
            return -1
        if array[left] < array[mid]:
            if array[left] <= target < array[mid]:
                return index_search(array, left, mid - 1, target)
            else:
                return index_search(array, mid + 1, right, target)
        if array[mid] < array[left]:
            if array[mid] < target <= array[right]:
                return index_search(array, mid + 1, right, target)
            else:
                return index_search(array, left, mid - 1, target)
        if array[mid] == array[left]:
            if array[mid] != array[right]:
                return index_search(array, mid + 1, right, target)
            else:
                result = index_search(array, left, mid - 1, target)
                if result == -1:
                    return index_search(array, mid + 1, right, target)
                else:
                    return result
        return -1

    start, end = 0, len(nums) - 1
    return index_search(nums, start, end, target)


def main():
    # n = int(input())
    # k = int(input())
    # array = input().split(' ')
    n = 9
    k = 100
    array = '19 21 100 101 1 4 5 7 12'.split(' ')
    # index = [None]
    for i in range(n):
        array[i] = int(array[i])
    answer = broken_search(array, k)
    print(answer)


if __name__ == '__main__':
    main()
