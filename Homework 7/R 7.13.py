def find(self, e):  # new methord to find the position on first e or none if not found
    if e in self._node._element:  # checks if e is in element
        x = 0
        y = self._header._next  # gets the first position
        while e != self._node._element[x]:  # runs until it reaches the element e
            x += 1
            y = y._next  # keeps changing the position
        return self._make_position(y._next)  # gets the position and returns the position
    else:  # returns non if not found
        return None
