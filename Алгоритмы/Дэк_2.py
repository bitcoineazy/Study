# Дэк - очередь с двумя концами
class Deque:
    def __init__(self, n):
        self.tail = 0
        self.size = 0
        self.max_size = n
        self.deque = [None] * n

    def push_front(self, value):
        if self.get_size() < self.max_size:
            if self.get_size() == 0:
                self.tail = 0
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def push_back(self, value):
        if self.get_size() < self.max_size:
            for i in range(self.tail - 1, -1, -1):
                self.deque[(i + 1) % self.max_size] = self.deque[i]
            self.deque[0] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.get_size() > 0:
            pop_front = self.deque[self.tail - 1]
            self.deque[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            print(pop_front)
        else:
            print('error')

    def pop_back(self):
        if self.get_size() > 0:
            pop_back = self.deque[0]
            for i in range(self.tail):
                self.deque[i] = self.deque[i + 1]
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            print(pop_back)

        else:
            print('error')


    def get_size(self):
        return self.size


def main():
    n = int(input())
    max_size = int(input())
    commands = [input() for i in range(n)]

    deck = Deque(max_size)
    for i in commands:
        if 'push_front' in i:
            deck.push_front(i.split()[1])
        if 'push_back' in i:
            deck.push_back(i.split()[1])
        if 'pop_front' in i:
            deck.pop_front()
        if 'pop_back' in i:
            deck.pop_back()
        # print(i, deck.deque)
    # print(deck.deque)


if __name__ == '__main__':
    main()
