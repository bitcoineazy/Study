from tkinter import *
from tkinter import filedialog as fd
import random
import keyboard
import time



time_passed = []
cycles = []
dist_1 = []
dist_2 = []
distz = {}



class Circles:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval([self.x1, self.y1], [self.x2, self.y2], fill="red")
        self.attempts = 0

        self.coords = self.canvas.coords(self.ball)

        self.time_start = time.time()

    def move_ball_1(self):

        self.start_cord = self.coords[0]
        deltax = 1
        deltay = 0
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(100, self.move_ball_1)

        dist_1.append(self.canvas.coords(self.ball))
        #self.end_cord = d
        distz.update({time.time()-self.time_start:self.canvas.coords(self.ball)})


    def move_ball_2(self):
        deltax = -1
        deltay = 0
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(100, self.move_ball_2)
        dist_2.append(1)
        self.end_cord = self.canvas.coords(self.ball)


    def refresh_ball(self):
        self.time_refresh = time.time()
        self.canvas.delete('all')
        self.ball1 = Circles(self.canvas, 0, 250, 50, 300) #0, 0, 50, 50 - края
        self.ball2 = Circles(self.canvas, 500, 250, 450, 300) #450, 450, 500, 500


        self.ball1.move_ball_1()
        self.ball2.move_ball_2()


    def show_range(self):
        centre_1 = 25
        centre_2 = 475

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
        self.circles_save = Button(self.circles_window, text='Сохранить результаты', command=self.save_button, width=len('Сохранить результаты'))
        self.circles_begin_button.grid(row=0, column=0)
        self.circles_save.grid(row=0, column=1)

    def circles_logic(self):
        self.circles_test = Toplevel(self.circles_window)
        self.canvas = Canvas(self.circles_test, width=500, height=500)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind_all('<space>', self.circle_test)
        self.time_reaction = time.time()
        self.ball1 = Circles(self.canvas, 0, 250, 50, 300)
        self.ball2 = Circles(self.canvas, 500, 250, 450, 300)


    def circle_test(self, event):
        '''if event.char == event.keysym:
            msg = 'Normal Key %r' % event.char
            print(msg)'''
        #print(event)
        #print(time.time() - self.time_reaction)

        self.ball1.refresh_ball()
        self.ball2.refresh_ball()
        #self.canvas.delete('all')
        self.show_range()
        #print(self.ball1.x1, self.ball1.x2)
        self.show_dist()
    def show_range(self):
        '''centre_1 = 25
        centre_2 = 475
        for i in range(len(time_passed)):
            print(time.time() - time_passed[i])'''
        self.range = 0
        print(dist_1[-1])
        print(distz)
        #print((475 - len(dist_2)) - (len(dist_1)+25))
        '''for value in distz.values():
            print(value)'''

    '''def dist(pt1, pt2):
        return ((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2) ** .5'''


        #print(len(cycles))
        #print(range - len(cycles))

        #print(len(cycles) - len(cycles[0:-2]))

    def show_dist(self):
        #print(len(cycles) - self.range)
        print(len(cycles))

    def instruction(self):
        help_texts = 'Тест запускается при нажатии на SPACE'
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
