from math import sqrt


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = [['_'] * 20 for _ in range(20)]

    def print_screen(self, board):
        self.screen = board
        for line in board:
            for symb in line:
                print(symb, end=' ')
            print()

    def update_board(self, board):
        self.screen = board

    def get_board(self):
        board = self.screen

    def draw_figures(self):
        triangle1 = Triangle(Figure(2, 2), Figure(2, 19), Figure(10, 2))
        square = Square(Figure(0, 0), Figure(10, 0), Figure(0, 10), Figure(10, 10))
        triangle1.draw()
        #triangle1.print_screen(triangle1.screen)
        square.draw()
        #square.print_screen(square.screen)
        Boardz().draw_board()


class Triangle(Figure):
    def __init__(self, sh1, sh2, sh3):
        self.sh1 = sh1
        self.sh2 = sh2
        self.sh3 = sh3
        #self.screen = [['_'] * 20 for _ in range(20)]

    def redraw_table(self):
        pass

    def draw(self):
        #screen = [['_'] * 20 for _ in range(20)]
        self.screen = [['_'] * 20 for _ in range(20)]
        board = Boardz()
        board.line(self.sh1, self.sh2)
        board.line(self.sh1, self.sh3)
        board.line(self.sh2, self.sh3)
        #Board.update_board(self.screen)

    def area(self):
        a = sqrt((self.sh1.x - self.sh2.x) ** 2 + (self.sh1.y - self.sh2.y) ** 2)
        b = sqrt((self.sh1.x - self.sh3.x) ** 2 + (self.sh1.y - self.sh3.y) ** 2)
        c = sqrt((self.sh2.x - self.sh3.x) ** 2 + (self.sh2.y - self.sh3.y) ** 2)
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s


class Square(Triangle):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        '''self.screen = [['_'] * 20 for _ in range(20)]
        super().line(self.x1, self.x2)
        super().line(self.y1, self.y2)
        super().line(self.x1, self.y1)
        super().line(self.x2, self.y2)
        super().update_board(self.screen)'''
        pass


class Boardz(Figure):
    def __init__(self, board):
        self.board = [['_'] * 20 for _ in range(20)]

    def draw_board(self):
        for line in self.board:
            for symb in line:
                print(symb, end=' ')
            print()

    def line(self, sh1, sh2):
        #board = self.screen
        L=(max(sh2.x-sh1.x,sh2.y-sh1.y))+1
        dx = (sh2.x-sh1.x) / L if L!=0 else 0
        dy = (sh2.y-sh1.y) / L if L!=0 else 0
        y = sh1.y
        x = sh1.x
        for i in range(0,L):
            self.board[round(y)][round(x)]='*'
            y+=dy
            x+=dx
        self.board[sh2.y][sh2.x]='*'




class Board:
    def __init__(self):
        self.board = [['_'] * 20 for _ in range(20)]

    def print_board(self):
        for line in self.board:
            for symb in line:
                print(symb, end=' ')
            print()

    def draw_triangle(self, sh1, sh2, sh3):
        self.line(sh1, sh2)
        self.line(sh1, sh3)
        self.line(sh2, sh3)
        #self.print_board()

    def draw_square(self, x1, x2, y1, y2):
        self.line(x1, x2)
        self.line(y1, y2)
        self.line(x1, y1)
        self.line(x2, y2)
        #self.print_board()

    def draw_rhombus(self, x1, x2, x3, x4):
        self.line(x1, x2)
        self.line(x2, x3)
        self.line(x4, x3)
        self.line(x1, x4)


    def move_figures(self, **ways):
        for direction, length in ways.items():
            if 'up' in direction:
                print(self.board[0])


                for i in range(len(self.board)):
                    #print(self.board)
                    if '*' in self.board[i]:
                        x = self.board[i].count('*')
                        self.board[i].insert(x, '*')
                        self.board[i].pop(self.board[i].index('*'))

                    #self.board[index][length] = '!'


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
    #board.move_figures(up=5)
    board.print_board()










#triangle = Triangle(Figure(2, 2), Figure(2, 19), Figure(10, 2))
#triangle.draw()
#print(triangle.area())
#triangle.print_screen()
#new = Figure(0,0)
#new.draw_figures()
#new.print_screen()