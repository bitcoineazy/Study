def list3_to2(list1, list2, list3):
    new_list_1 = []
    new_list_2 = []
    length = len(list1) + len(list2) + len(list3)
    for i in range(length):
        if i > len(list1) - 1:
            if i > (length // 2) - 1:
                if i > (len(list1) + len(list2)) - 1:
                    new_list_2.append(list3[i % len(list3)])
                else:
                    new_list_2.append(list2[i % len(list2)])
            else:
                new_list_1.append(list2[i % len(list2)])
        else:
            new_list_1.append(list1[i % len(list1)])
    return new_list_1, new_list_2


def main():
    list_1 = [1, 2, 3, 4, 5, 97, 1000]
    list_2 = [6, 7, 8, 9, 10, 98, 1001]
    list_3 = [11, 12, 13, 14, 15, 99, 1002]
    print(list3_to2(list_1, list_2, list_3))


if __name__ == '__main__':
    main()
