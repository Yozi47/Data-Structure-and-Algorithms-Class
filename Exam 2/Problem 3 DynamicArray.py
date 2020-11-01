import ctypes


class DynamicArray(object):

    def __init__(self):
        self._n = 0
        self._capacity = float(1)
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()
        # creates an "array" of pointers
        # http://docs.python.org/3/c-api/structures.html#c.PyObject

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        if not 0 <= item < self._n:
            raise IndexError('invalid index')
        return self._A[item]

    # GROW THE ARRAY DYNAMICALLY
    def _resize(self, c):    # c should be larger that the original array
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        if self._n == self._capacity:    # list is full
            self._resize(self._capacity + int(self._capacity/4))   # grow the "list" by twice its size
        self._A[self._n] = obj
        self._n += 1

    # Insert...
    # assume 0<= k < n
    def insert(self, k, value):
        if self._n == self._capacity:   # out of empty cells, must make room
            self._resize(self._capacity + self._capacity/4)

        for j in range(self._n, k, -1):   # shift rightmost object first
            self._A[j] = self._A[j-1]

        self._A[k] = value
        self._n += 1


    def pop(self):
        if self._n > 1:
            self._A[self._n - 1] = None     # help garbage collection
            self._n -= 1

        # optimize memory usage by shrinking the capacity
        if self._n < self._capacity // 4:
            self._resize(self._capacity // 2)



if __name__ == '__main__':
    import time
    A = DynamicArray()
    start = time.time()
    for i in range(20):
        A.append(i)
    end = time.time()
    print("Time taken: ", end - start)



















