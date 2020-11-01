def concatenate(self, Q2):  # this methord concatenate queue Q2 in a regular queue
    if self.is_empty():  # checks if the queue is empty
        self._head = Q2._head  # if queue is empty then assign queue Q2 in queue
    else:  # if queue is not empty then take the last position and add queue Q2 to the end of queue
        self._tail._next = Q2._head
    Q2._head = None  # Q2 is assigned as empty queue