# C 5.16
def pop(self):
    if self._n > 1:  # check if the array has 1 or more elements
        new_list = []  # A empty list to get the new list after poping an item
        for i in range(self._n-2):  # looping through the number of element except last one
            new_list.append(self._A[i])  # adding the element in new list except the last element
        self._A = new_list  # making the list self._A as new obtained list
    self._n -= 1  # decreasing the length of list
    if self._n < self._capacity/4:  # checking if the length of array is less than one forth of full capacity
        self._capacity = self._capacity/2  # if above condition is true then new capacity is half the actual capacity.
