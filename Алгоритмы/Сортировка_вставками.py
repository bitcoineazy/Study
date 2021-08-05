def insertion_sort(array):
    for i in range(len(array) - 1):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')
    return array

print(insertion_sort([9, 12, 64, 6, 9]))
