class StackCalculator:
    def __init__(self):
        self.calc_stack = []

    def push(self, x):
        self.calc_stack.append(int(x))

    def calculate_expression(self, expression):
        for i in expression.split():
            if i == '+':
                x, y = self.calc_stack.pop(), self.calc_stack.pop()
                self.push(x + y)
            if i == '*':
                x, y = self.calc_stack.pop(), self.calc_stack.pop()
                self.push(x * y)
            if i == '-':
                x, y = self.calc_stack.pop(), self.calc_stack.pop()
                self.push(y - x)
            if i == '/':
                x, y = self.calc_stack.pop(), self.calc_stack.pop()
                self.push(y // x)
            else:
                try:
                    self.push(i)
                except ValueError:
                    pass
        return self.calc_stack[-1]


def main():
    calculator = StackCalculator()
    print(calculator.calculate_expression(input()))


main()
