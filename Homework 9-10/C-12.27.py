def merge(self, b):
    self._tail._next = b._head
    self._node._element = sorted(self._node._element)
    b._head = None