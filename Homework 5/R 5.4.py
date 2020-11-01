def __getitem__(self, k):
    if k >= 0 and k < self._n:
        return self._A[k]  # return the item at k position
    else:
        raise IndexError("invalid index")  # raise error if the number is less than 0 or more than the length of list