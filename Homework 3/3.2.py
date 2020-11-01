"""R-3.2 The number of operations executed by algorithms A and B is 8nlogn and 2n2,
respectively. Determine n0 such that A is better than B for n ≥ n0."""

"""Taking A and B from question and equating,
    8nlogn = 2n**2
    4nlogn = n**2  Taking off 2 from both side
    4 = n/logn
    Solving for n,
    No = 16, since all n > 16, A will be faster than B
    """