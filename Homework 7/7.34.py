def swap(self, p, q):  # methord swap the element in the position p to q and vice versa
    orginal_p = self._validate(p)
    orginal_q = self._validate(q)
    old_p = orginal_p._element  # temporarily store old p element
    old_q = orginal_q._element  # temporarily store old q element
    orginal_p._element = old_q  # replaces with q element
    orginal_q._element = old_p  # replaces with q element