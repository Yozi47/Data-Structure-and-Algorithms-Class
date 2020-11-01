# Abstract Data Type : Circularly Linked List
# A circularly linked list CLL supports
# All methods of linked list
# tail._next = head

class CLinkedList:
    #--- NODE CLASS ---
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, _element, _next):
            self._element = _element
            self._next = _next

        def getElement(self):
            return self._element

        def getNext(self):
            return self._next


    #---- ERROR CLASS ----
    class Empty(Exception):
        pass

    #--- CONSTRUCTOR ---

    def __init__(self):
        self._current = None
        self._size = 0

    def __len__(self):
        return self._size


    def is_empty(self):
        return len(self) == 0

    def current(self):
        if self._current is not None:
            return self._current.getElement()
        else:
            return self._current

    def next(self):
        if self.is_empty():
            raise self.Empty("Linked list is empty.")
        if self._size > 1:    # at least two elements
            self._current = self._current.getNext()
        return self.current()

    def insert(self, e):
        """Insert e after current element and update."""
        if self._current is not None:
            new_node = self._Node(e, self._current.getNext())
            self._current._next = new_node
            self._current = new_node
        else:
            new_node = self._Node(e, self._current)
            self._current = new_node
            self._current._next = new_node
        self._size += 1


    def remove(self):
        """Removes and returns the element after current, or current if its the only element."""
        if self.is_empty():
            raise self.Empty("Linked list is empty.")
        elif self._size == 1:
            temp = self._current
            self._current = None
        elif self._size == 2:
            temp = self._current._next
            self._current._next = self._current
        else:
            temp = self._current._next
            self._current._next = self._current._next._next
        self._size -= 1
        return temp.getElement()


    '''Function for Exam Question no 1'''
    def count(self):
        count = 0  # initiating a counter as 0
        x = self._current.getElement()  # gives the current position element
        y = None  # assuming as a none item first
        while y != x:  # checking for same position
            self._current = self._current._next  # takes next position to current position
            y = self._current.getElement()  # gets the element for current position
            count += 1  # counts until the same element is found which gives the length of the list
        return count

if __name__ == "__main__":
    # Sample for creating CLinked List
    CLL = CLinkedList()
    CLL.insert("A")
    CLL.insert("B")
    CLL.insert("C")
    CLL.insert("D")
    CLL.insert("E")
    CLL.insert("F")
    print("Output by using len function: ", len(CLL))
    print("Output by using count function: ", CLL.count())

