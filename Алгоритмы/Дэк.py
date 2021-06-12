# Дэк - очередь с двумя концами
class Deque:
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = n
        self.queue = [None] * n

    def push_front(self, value: int):
        if self.size < self.max_size:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def push_back(self, value: int):
        if self.size < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        pop_front = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return pop_front

    def pop_back(self):
        if self.is_empty():
            return 'error'
        pop_back = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return pop_back

    def is_empty(self):
        return self.size == 0


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
            print(deck.pop_front())
        if 'pop_back' in i:
            print(deck.pop_back())


if __name__ == '__main__':
    main()
