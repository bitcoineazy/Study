# Очередь основана на концепции FIFO - First in First out
class Queue:  # Очередь на кольцевом буфере, Сложность: O(1)
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
        # В пустой очереди и голова, и хвост указывают на ячейку с индексом 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    # Хвост всегда указывает на первую свободную для записи ячейку,
    # а голова — на элемент, добавленный в очередь раньше всех остальных
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


q = Queue(8)
q.push(1)
print(q.queue)  # [1, None, None, None, None, None, None, None]
print(q.size)  # 1
q.push(-1)
q.push(0)
q.push(11)
print(q.queue)  # [1, -1, 0, 11, None, None, None, None]
print(q.size)  # 4

q.pop()
print(q.queue)  # [None, -1, 0, 11, None, None, None, None]
print(q.size)  # 3

q.pop()
q.pop()
q.push(-8)
q.push(7)
q.push(3)
q.push(16)
print(q.queue)  # [None, None, None, 11, -8, 7, 3, 16]
print(q.size)  # 5
q.push(12)
# Когда пытаемся переполнить очередь, хвост будет указывать на след ячейку по часовой стрелке - 0
print(q.queue)  # [12, None, None, 11, -8, 7, 3, 16]
print(q.size)  # 6
