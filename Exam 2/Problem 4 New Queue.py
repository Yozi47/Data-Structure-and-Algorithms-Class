from Stacks import ArrayStack
class Empty(Exception):
    pass

class new_Queue:
    def __init__(self):
        self.data = ArrayStack()
        self.data2 = ArrayStack()

    def enqueue(self, e):
        return self.data.push(e)

    def dequeue(self):
        while not self.data.is_empty():
            self.data2.push(self.data.pop())
        out = self.data2.pop()
        while not self.data2.is_empty():
            self.data.push(self.data2.pop())
        return out

    def first(self):
        while not self.data.is_empty():
            self.data2.push(self.data.pop())
        out = self.data2.top()
        while not self.data2.is_empty():
            self.data.push(self.data2.pop())
        return out

    def is_empty(self):
        return self.data.is_empty()

    def len(self):
        return len(self.data)

