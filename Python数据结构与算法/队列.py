class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return  self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(11.1)
print(q.size())
q.dequeue()
print(q.size())
print(q.isEmpty())