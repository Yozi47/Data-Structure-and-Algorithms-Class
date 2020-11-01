
"""R-3.15 Show that f(n) is O(g(n)) if and only if g(n) is Ω(f(n)). """

"""From definition of Big-oh notation
    f(n) = g(n) has constant Co > 0 and constant No
    such that n >= No : g(n) >= (1/Co)*f(n)
    Here, Co > 0, so that the constant (1/Co)>0
    Hence, there exist a constant k > 0, where k = (1/Co)
    and a constant No, Such that n>= No: g(n) >= k* f(n)
    which is the definition of g(n) = Ω(f(n))"""
