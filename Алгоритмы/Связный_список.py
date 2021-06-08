class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


# У каждого элемента есть значение и ссылка на следующий элемент списка
n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)
print_linked_list(n1)  # вершина n1
print_linked_list(n2)  # вершина n2


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


# Добавление нового элемента по индексу
def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


node, index, value = n1, 2, 'new_node'
head = insert_node(node, index, value)
print_linked_list(head)


# Удаление элемента по индексу
def del_node(head, index):
    if index == 0:
        head = get_node_by_index(head, 1)
        return head
    previous_node = get_node_by_index(head, index - 1)
    next_node = get_node_by_index(head, index + 1)
    previous_node.next = next_node
    return head


node, index = n1, 2
head = del_node(node, index)
print_linked_list(head)


# Поиск индекса по значению
def find_val(node, value):
    index = 0
    while node:
        if node.value == value:
            return index
        node = node.next
        index += 1
    else:
        return -1


head, value = n1, 'third'
print(find_val(head, value))



