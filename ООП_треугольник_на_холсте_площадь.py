class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = [['*'] * 20 for _ in range(20)]

    def print_screen(self):
        for line in self.screen:
            for symb in line:
                print(symb, end=' ')
            print()


class Triangle(Figure):
    def __init__(self, sh1, sh2, sh3):
        self.sh1 = sh1
        self.sh2 = sh2
        self.sh3 = sh3
        self.screen = [['.'] * 20 for _ in range(20)]

    def line(self, sh1, sh2):
        L = (max(sh2.x - sh1.x, sh2.y - sh1.y)) + 1
        dx = (sh2.x - sh1.x) / L if L != 0 else 0
        dy = (sh2.y - sh1.y) / L if L != 0 else 0
        y = sh1.y
        x = sh1.x
        for i in range(0, L):
            self.screen[round(y)][round(x)] = '*'
            y += dy
            x += dx
        self.screen[sh2.y][sh2.x] = '*'

    def draw(self):
        self.screen = [['_'] * 40 for _ in range(20)]
        self.line(self.sh1, self.sh2)
        self.line(self.sh1, self.sh3)
        self.line(self.sh2, self.sh3)
        self.print_screen()

    def area(self):
        from math import sqrt
        a = sqrt((self.sh1.x - self.sh2.x) ** 2 + (self.sh1.y - self.sh2.y) ** 2)
        b = sqrt((self.sh1.x - self.sh3.x) ** 2 + (self.sh1.y - self.sh3.y) ** 2)
        c = sqrt((self.sh2.x - self.sh3.x) ** 2 + (self.sh2.y - self.sh3.y) ** 2)
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s


triangle = Triangle(Figure(2, 2), Figure(2, 19), Figure(38, 2))
triangle.draw()
print(triangle.area())