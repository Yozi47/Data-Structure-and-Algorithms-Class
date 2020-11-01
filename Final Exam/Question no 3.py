'''
Let us consider the base case as  H = 0.
Here a binary tree has height 0 which has single node.
so we get, 1=2^0
Therefore, the base case is satisfied as of the induction hypothesis.

Using Induction
Let us assume, T be a binary tree of height k+1.
So the subtrees of binary trees of height <= k,
using Induction Hypothesis it has at most 2^k leaves.
The number of leaves in T is equal to T's subtrees which is less
than or equal to
2^k + 2^k = 2^(k+1).
Hence the hypothesis is true for k+1, so the theorem is proved.
'''