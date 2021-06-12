class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(int(x))

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print('error')


def main():
    stack = Stack()
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: y - x, '*': lambda x, y: x * y, '/': lambda x, y: y // x}
    expression = input()
    for i in expression.split():
        try:
            stack.push(i)
        except ValueError:
            x, y = stack.pop(), stack.pop()
            stack.push(operations[i](x, y))
    answer = stack.items[-1]
    print(answer)
    # print(answer expression('3 10 5 / +'))  # 10 / 5 = 2, 3 + 2 = 5
    # print(answer expression('5 4 3 2 1 * * * *'))  # fact(5) = 120


main()
