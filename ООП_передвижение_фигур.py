
class Board:
    def __init__(self):
        self.board = [['_'] * 20 for _ in range(20)]
        self.coord = {}

    def print_board(self):
        for line in self.board:
            for symb in line:
                print(symb, end=' ')
            print()

    def draw_triangle(self, sh1, sh2, sh3):
        self.line(sh1, sh2)
        self.line(sh1, sh3)
        self.line(sh2, sh3)
        self.coord.update({'triangle': [sh1.x, sh1.y, sh2.x, sh2.y, sh3.x, sh3.y]})

    def draw_square(self, x1, x2, y1, y2):
        self.line(x1, x2)
        self.line(y1, y2)
        self.line(x1, y1)
        self.line(x2, y2)
        self.coord.update({'square': [x1.x, x1.y, x2.x, x2.y, y1.x, y1.y, y2.x, y2.y]})

    def draw_rhombus(self, x1, x2, x3, x4):
        self.line(x1, x2)
        self.line(x2, x3)
        self.line(x4, x3)
        self.line(x1, x4)
        self.coord.update({'rhombus': [x1.x, x1.y, x2.x, x2.y, x3.x, x3.y, x4.x, x4.y]})

    def move_figures(self, up=None, right=None, left=None, down=None):
        print(self.board[0])
        print(self.coord)
        self.board = [['_'] * 20 for _ in range(20)]
        self.draw_square(Coords(self.coord['square'][0]+(right if right else 0) - (left if left else 0), self.coord['square'][1]+(up if up else 0) - (down if down else 0)),
                         Coords(self.coord['square'][2]+(right if right else 0) - (left if left else 0), self.coord['square'][3]+(up if up else 0) - (down if down else 0)),
                         Coords(self.coord['square'][4]+(right if right else 0) - (left if left else 0), self.coord['square'][5]+(up if up else 0) - (down if down else 0)),
                         Coords(self.coord['square'][6]+(right if right else 0) - (left if left else 0), self.coord['square'][7]+(up if up else 0) - (down if down else 0)))
        self.draw_triangle(Coords(self.coord['triangle'][0]+(right if right else 0) -(left if left else 0), self.coord['triangle'][1]+(up if up else 0) - (down if down else 0)),
                           Coords(self.coord['triangle'][2]+(right if right else 0) -(left if left else 0), self.coord['triangle'][3]+(up if up else 0) - (down if down else 0)),
                           Coords(self.coord['triangle'][4]+(right if right else 0) -(left if left else 0), self.coord['triangle'][5]+(up if up else 0) - (down if down else 0)))
        self.draw_rhombus(Coords(self.coord['rhombus'][0]+(right if right else 0) -(left if left else 0), self.coord['rhombus'][1]+(up if up else 0) - (down if down else 0)),
                          Coords(self.coord['rhombus'][2]+(right if right else 0) -(left if left else 0), self.coord['rhombus'][3]+(up if up else 0) - (down if down else 0)),
                          Coords(self.coord['rhombus'][4]+(right if right else 0) -(left if left else 0), self.coord['rhombus'][5]+(up if up else 0) - (down if down else 0)),
                          Coords(self.coord['rhombus'][6]+(right if right else 0) -(left if left else 0), self.coord['rhombus'][7]+(up if up else 0) - (down if down else 0)))


    def line(self, sh1, sh2):
        # board = self.screen
        L = (max(sh2.x - sh1.x, sh2.y - sh1.y)) + 1
        dx = (sh2.x - sh1.x) / L if L != 0 else 0
        dy = (sh2.y - sh1.y) / L if L != 0 else 0
        y = sh1.y
        x = sh1.x
        for i in range(0, L):
            self.board[round(y)][round(x)] = '*'
            y += dy
            x += dx
        self.board[sh2.y][sh2.x] = '*'

class Coords(Board):
    def __init__(self, x, y):
        self.x = x
        self.y = y



if __name__ == '__main__':
    board = Board()
    board.draw_triangle(Coords(2, 2), Coords(2, 19), Coords(10, 2))
    board.draw_square(Coords(0, 0), Coords(10, 0), Coords(0, 10), Coords(10, 10))
    board.draw_rhombus(Coords(5, 5), Coords(10, 10), Coords(15, 5), Coords(10, 0))
    board.move_figures(right=3)
    board.print_board()










