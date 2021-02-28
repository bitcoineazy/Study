from tkinter import *
from ipaddress import IPv4Address
import re


class MyIPv4(IPv4Address):
    def __and__(self, other: IPv4Address):
        '''__and__ позволяет использовать бинарный оператор &, чтобы применять маску к IP-адресу'''
        if not isinstance(other, (int, IPv4Address)):
            raise NotImplementedError
        return self.__class__(int(self) & int(other))
    @property
    def binary_repr(self, sep=".") -> str:
        '''Представляет IPv4 в виде 4 блоков по 8 бит.'''
        return sep.join(f"{i:08b}" for i in self.packed)
    @classmethod
    def from_binary_repr(cls, binary_repr: str):
        """Создает IPv4 из двоичного представления."""
        i = int(re.sub(r"[^01]", "", binary_repr), 2)  # 14 строка
        return cls(i)


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
        h = 76
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

    def define_class(self, first_octet):
        if 1 <= first_octet <= 126:
            self.your_class_entry.insert(END, 'A-класс')
        elif 128 <= first_octet <= 191:
            self.your_class_entry.insert(END, 'B-класс')
        elif 192 <= first_octet <= 223:
            self.your_class_entry.insert(END, 'C-класс')
        elif 224 <= first_octet <= 239:
            self.your_class_entry.insert(END, 'D-класс')
        elif 240 <= first_octet <= 247:
            self.your_class_entry.insert(END, 'E-класс')
        else:
            self.your_class_entry.insert(END, 'Не принадлежит ни одному из классов')

    def calculate_net(self):
        ip_entry = self.ip_v4.get()
        musk_entry = self.musk.get()
        self.answer_net_10 = Entry(self)
        self.answer_net_2 = Entry(self, width=35)
        self.your_class_entry = Entry(self)
        if len(ip_entry) < 16: #проверка десятичный или двоичный IP-адрес по длине
            NET_answer = MyIPv4(ip_entry) & MyIPv4(musk_entry)
            self.answer_net_10.insert(END, NET_answer)
            self.answer_net_2.insert(END, str(NET_answer.binary_repr))
            octets = str(NET_answer).split('.')
            self.define_class(int(octets[0]))
        else:
            NET_answer = MyIPv4.from_binary_repr(ip_entry) & MyIPv4.from_binary_repr(musk_entry)
            self.answer_net_10.insert(END, NET_answer)
            self.answer_net_2.insert(END, NET_answer.binary_repr)
            octets = str(NET_answer).split('.')
            self.define_class(int(octets[0]))
        self.your_net_10 = Label(self, text='Ваш NET-адрес(10): ')
        self.your_net_2 = Label(self, text='Ваш NET-адрес(2): ')
        self.your_class = Label(self, text='Ваш класс сети: ')
        self.your_net_10.grid(row=0, column=4)
        self.your_net_2.grid(row=1, column=4)
        self.answer_net_10.grid(row=0, column=5)
        self.answer_net_2.grid(row=1, column=5)
        self.your_class.grid(row=2, column=4)
        self.your_class_entry.grid(row=2, column=5)


def main():
    root = Tk()
    ex = IPCalculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()