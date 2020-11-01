def insert(self,k,value):
    if self._n == self._capacity:  # not enough room
        self._capacity += 1  # Adding one more space to fit the element
    for j in range(self._n, k, -1):  # shift rightmost first
        self._A[j] = self._A[j-1]
    self._A[k] = value
    self._n += 1  # store newest element

