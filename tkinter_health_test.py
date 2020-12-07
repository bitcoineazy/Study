from tkinter import *
from tkinter import filedialog as fd
import random
import keyboard
import time


class Circles:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval([self.x1, self.y1], [self.x2, self.y2], fill="red")

    def move_ball_1(self):
        deltax = 1
        deltay = 1
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(10, self.move_ball_1)

    def move_ball_2(self):
        deltax = -1
        deltay = -1
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(10, self.move_ball_2)


class HealthTest(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title('Тест Здоровья')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.test_circles = Button(self, text='Тест Точность', command=self.circles, width=16)
        self.instruction = Button(self, text='Инструкция', command=self.instruction, width=16)
        self.test_circles.grid(row=0, column=0)
        self.instruction.grid(row=0, column=1)

    def circles(self):
        self.circles_window = Toplevel(self)
        self.circles_begin_button = Button(self.circles_window, text='Начать тест', command=self.circles_logic, width=16)
        self.circles_save = Button(self.circles_window, text='Сохранить результаты', command=self.save_button, width=16)
        self.circles_begin_button.grid(row=0, column=0)
        self.circles_save.grid(row=0, column=1)

    def circles_logic(self):
        self.circles_test = Toplevel(self.circles_window)
        self.canvas = Canvas(self.circles_test, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        ball1 = Circles(self.canvas, 0, 0, 50, 50)
        ball2 = Circles(self.canvas, 450, 450, 500, 500)
        ball1.move_ball_1()
        ball2.move_ball_2()
        self.canvas.bind('<>', self.circle_test)

    def circle_test(self):
        pass



    def instruction(self):
        help_texts = '123'
        self.instruction_window = Toplevel(self)
        self.help_text = Text(self.instruction_window)
        self.help_text.insert(1.0, help_texts)
        self.help_text.grid(row=0, column=0)

    def save_button(self):
        files = [('CSV Files', '*.csv'),
                 ('Text Document', '*.txt'),
                 ('Pickle Files', '*.pkl')]
        file_name = fd.asksaveasfile(filetypes=files, defaultextension=files)
        #file_name.write()

    def centerWindow(self):
        w = 244
        h = 26
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    ex = HealthTest(root)
    root.mainloop()

if __name__ == '__main__':
    main()
