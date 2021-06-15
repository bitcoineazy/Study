class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(int(x))

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('pop from an empty list')


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def main():
    stack = Stack()
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: y - x,
                  '*': lambda x, y: x * y, '/': lambda x, y: y // x}
    expression = input()
    for i in expression.split():
        if is_number(i):
            stack.push(i)
        else:
            x, y = stack.pop(), stack.pop()
            stack.push(operations[i](x, y))
    answer = stack.pop()
    print(answer)


if __name__ == '__main__':
    main()
