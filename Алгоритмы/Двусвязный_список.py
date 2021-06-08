class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


node3 = DoubleConnectedNode("node3")
node2 = DoubleConnectedNode("node2")
node1 = DoubleConnectedNode("node1")
node0 = DoubleConnectedNode("node0")

node0.next = node1

node1.prev = node0
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


# Перевернуть двусвязный список
def reverse_double_linked_list(node):
    left = node
    right = node
    # Пройдите по списку и установите прямо
    # указатель на конец списка
    while right.next is not None:
        right = right.next
    # Поменять местами данные левого и правого указателя
    # и двигать их навстречу друг другу
    # пока они не встретятся или не пересекаются
    while left != right and left.prev != right:
        # Поменять местами данные левого и правого указателя
        t = left.value
        left.value = right.value
        right.value = t
        # Предварительный левый указатель
        left = left.next
        # Предварительный правый указатель
        right = right.prev
    return node


print_linked_list(node0)
reversed_list = reverse_double_linked_list(node0)
print_linked_list(reversed_list)
