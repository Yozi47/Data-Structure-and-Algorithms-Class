# Abstract Data Type : Queue
# Queue Q supports
# Q.enqueue(e) : add element e to the "back" of the queue Q
# Q.dequeue() : removes and returns the first element of the queue Q
# Q.first() : Return a reference to the first element of the queue Q
# Q.is_empty() : return true if Q does not contain any elements
# len(Q) : returns number of elements in Q

# The Adapted Design pattern: create a new class repackaging list methods

class Empty(Exception):
    pass


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



# Analysis:
# enqueue, dequeue -> O(1) amortized
# first, is_empty, len -> O(1)
































