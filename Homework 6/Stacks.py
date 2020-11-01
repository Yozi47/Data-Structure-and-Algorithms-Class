# Abstract Data Type : Stack
# Stack S Supports
# S.push(e) : add element e to the top of the stack S
# S.pop() : remove and return the top element of the stack
# S.top() : return a reference to the top element of stack S
# S.is_empty() : return True if S does not contain any elements
# len(S) : return number of elements of stack S

# We will use Python lists to implement a stack since lists implement append() and pop()
# This approach of creating a new class by "re-packaging" an existing data structure is called
# the Adapter Design Pattern

# Stack -> List
# push() -> append()
# pop() -> pop()
# top() -> L[-1]
# is_empty() -> len(L) == 0 or L == []
# len() -> len()


class Empty(Exception):
    """Simple Exception Extension."""
    pass

class ArrayStack(object):
    """LIFO STACK"""

    def __init__(self):
        self._data = []    # meant as a non-public instance

    def __repr__(self):
        return '%s' % self._data

    def __len__(self):     # allows the use of len()
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        """"Raise Exception if stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data[-1]

    def pop(self):
        """"Raise Exception if stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data.pop()

# Analysis: based on running times of list methods (see table 5.4)
# push() and pop() -> O(1) amortized (mutable)
# top(), is_empty(), len() -> O(1)   (immutable)
    






























