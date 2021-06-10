# Дэк - очередь с двумя концами
class Deck:
    def __init__(self, n):
        self.head_front = 0
        self.head_back = n - 1
        self.tail_front = 0
        self.tail_back = n - 1
        self.size = 0
        self.max_size = n
        self.first_elem = 0
        self.last_elem = 0
        self.queue = [None] * n

    def push_front(self, value):
        if self.get_size() < self.max_size:
            self.queue[self.tail_front] = value
            self.tail_front = (self.tail_front + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def push_back(self, value):
        if self.get_size() < self.max_size:
            self.queue[self.tail_back] = value
            self.tail_back = (self.tail_back - 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.get_size() > 0:
            pop_front = self.queue[self.head_front]
            if pop_front is None:
                '''print(self.queue[self.tail_back - 1])
                self.queue[self.tail_back - 1] = None
                self.tail_back += (self.tail_back - 1) % self.max_size
                self.size -= 1'''
                print(self.queue[self.head_back])
                self.queue[self.head_back] = None
                self.head_back = (self.head_back - 1) % self.max_size
                self.size -= 1
            else:
                print(self.queue[self.tail_front - 1])
                self.queue[self.tail_front - 1] = None
                # self.head_front = (self.head_front + 1) % self.max_size
                self.tail_front = (self.tail_front - 1) % self.max_size
                self.size -= 1
        else:
            print('error')

    def pop_back(self):
        if self.get_size() > 0:
            pop_back = self.queue[self.head_back]
            if pop_back is None:
                #print('123')
                print(self.queue[self.head_front])
                self.queue[self.head_front] = None
                self.head_front = (self.head_front + 1) % self.max_size
                self.size -= 1
            else:
                '''print('345')
                print(self.queue)
                print(self.queue[self.tail_back])
                self.queue[self.tail_back] = None
                # self.head_back = (self.head_back - 1) % self.max_size
                self.tail_back = (self.tail_back + 1) % self.max_size
                self.size -= 1'''
                print(self.queue[(self.tail_back + 1) % self.max_size])
                self.queue[(self.tail_back + 1) % self.max_size] = None
                self.tail_back = (self.tail_back + 1) % self.max_size
                self.size -= 1
        else:
            print('error')

    def get_size(self):
        return self.size


def main():
    #n = int(input())
    #n = 4
    #max_size = int(input())
    max_size = 9
    #commands = [input() for i in range(n)]
    commands = ['push_back -977', 'pop_back', 'pop_back', 'push_front -86', 'pop_back', 'push_back 81', 'push_back 123', 'pop_front', 'pop_front', 'pop_back']
    deck = Deck(max_size)
    for i in commands:
        if 'push_front' in i:
            deck.push_front(i.split()[1])
        if 'push_back' in i:
            deck.push_back(i.split()[1])
        if 'pop_front' in i:
            deck.pop_front()
        if 'pop_back' in i:
            deck.pop_back()
        print(i, deck.queue)
    print(deck.queue)


main()
