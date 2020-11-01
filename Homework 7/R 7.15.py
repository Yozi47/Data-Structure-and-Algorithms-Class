def __reversed__(self):
    cursor = self.last()  # takes cursor to last
    while cursor is not None:  # checks the cursor for none
        yield cursor.element()
        cursor = self.before(cursor)  # gives the cursor one step before
