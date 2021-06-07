class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


# У каждого элемента есть значение и ссылка на следующий элемент списка
n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)
print_linked_list(n1)  # вершина n1
print_linked_list(n2)  # вершина n2
