def num_children(self, p):
    count = 0
    if self.left(p) is not None:
        count += self.left(p)
    if self.right(p) is not None:
        count += self.right(p)
    return count
