'''
Let us consider the base case as  H = 0.
Here a binary tree has height 0 which has single node.
so we get, 1=2^(0+1) -1
Therefore, the base case is satisfied as of the induction hypothesis.

Using Induction
Suppose the max modes in a binary tree of height h is
2**(h+1) -1 where h = 1, 2, .... , k
Assuming, T be a binary tree of height k+1.
So, the subtrees of binary trees of height <= k,
using Induction Hypothesis it has at most 2^(k+1)-1 nodes.
Total no of root node gives max modes in a binary tee of height k+1,
that means
2(2**(k+1)-1 + 1
2*2**(k+1)-2 + 1
2**((k+1)+1) - 1
Hence the hypothesis holds for k+1, so the theorem is proved.
'''