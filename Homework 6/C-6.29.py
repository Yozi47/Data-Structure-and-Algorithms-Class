class ArrayQueue(object):
    """Circular FIFO Queue."""
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0     # index of first element in queue

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        element_to_dequeue = self._data[self._front]
        self._data[self._front] = None    # for garbarge collection
        self._front = (self._front + 1) % len(self._data)   # use the size of underlying array (not the size of the queue)
        self._size -= 1
        if 0 < self._size < len(self._data) //4:  # num of elements in queue are less than a fourth of the capacity
            self._resize(len(self._data)//2)

        return element_to_dequeue


    def enqueue(self, e):
        if self._size == len(self._data):   # queue is full, must increase capacity
            self._resize(2*len(self._data))

        idx_to_enqueue = (self._front + self._size) % len(self._data)
        self._data[idx_to_enqueue] = e
        self._size += 1

    def _resize(self, capacity):
        temp = self._data
        self._data = [None] * capacity
        step = self._front
        for k in range(self._size):     # move existing elements only
            self._data[k] = temp[step]
            step = (1 + step) % len(temp)

        self._front = 0

    def __repr__(self):
        return '%s' % self._data


# Code for question no C-6.29 above code from Queues
    def rotate(self):
        data = self._data[0]  # picking the first element
        self._data[:-1] = self._data[1:]  # taking off all elements from second position
        self._data[-1] = data

if __name__ == '__main__':
    capacity = 6
    X = ArrayQueue(capacity)  # creating an empty Queue with capacity 6
    for i in range(capacity):  # adding elements in Queue
        X.enqueue(i)
    # printing the Queue
    print("Queue elements: ")
    print(X)
    # rotating the elements using rotate function and printing
    X.rotate()
    print("Queue elements after calling rotate function for once: ")
    print(X)
