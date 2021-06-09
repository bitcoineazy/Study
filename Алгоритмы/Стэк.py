# Стэк работает по принципу LIFO - Last in First out
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if len(self.items) > 0:
            print(max(i for i in self.items))
        else:
            print('None')


def main():
    n = int(input())
    commands = [input().split() for i in range(n)]
    stack = Stack()
    for i in commands:
        if len(i) > 1:
            stack.push(i[1])
        if 'pop' in i:
            stack.pop()
        if 'get_max' in i:
            stack.get_max()


main()
