from tkinter import *

class IPCalculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.parent.title("IP калькулятор")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def centerWindow(self):
        w = 732
        h = 51
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self):
        self.ip_entry = Label(self, text='IPv4 адрес: ')
        self.musk_entry = Label(self, text='Маска подсети: ')
        self.ip_entry.grid(row=0, column=0, sticky='w')
        self.musk_entry.grid(row=1, column=0, sticky='w')
        type_1 = IntVar()
        type_2 = IntVar()
        self.ip_v4 = Entry(self, textvariable=type_1)
        self.musk = Entry(self, textvariable=type_2)
        self.ip_v4.grid(row=0, column=1, sticky='n')
        self.musk.grid(row=1, column=1, sticky='n')
        self.calculate_butt = Button(self, text='Вычислить NET-адрес', command=self.calculate_net)
        self.calculate_butt.grid(row=0, column=3, sticky='w')


    def calculate_net(self):
        text = 0
        ip_entry = self.ip_entry.get()
        


        self.answer_net = Text(self, text=text)

def main():
    root = Tk()
    ex = IPCalculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()