class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.linked_queue = [Node()] * 1000

    def put(self, x):
        #temp = Node(x)
        #if self.head is None:
        #    self.head = temp
        #temp.next = self.tail
        #self.tail = temp
        self.linked_queue[self.tail] = Node(x)
        if self.get_size() > 1:
            self.linked_queue[self.tail-1].next = self.linked_queue[self.tail]
        self.tail = (self.tail + 1) % 1000
        self.size += 1

    def get(self):
        #print(self.head.value)
        if self.get_size() == 0:
            return 'error'
        else:
            x = self.linked_queue[self.head]
            self.linked_queue[self.head] = None
            self.head = (self.head + 1) % 1000
            self.size -= 1
            return x.value

    def get_size(self):
        return self.size


def main():
    #n = int(input())
    commands = ['put -34', 'put -35', 'put 40', 'get', 'get', 'get', 'size', 'get']
    #commands = [input() for i in range(n)]
    queue = LinkedQueue()
    for i in commands:
        if 'put' in i:
            queue.put(int(i.split()[1]))
        if 'get' in i:
            print(queue.get())
        if 'size' in i:
            print(queue.get_size())


main()
