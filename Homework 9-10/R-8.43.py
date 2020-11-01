'''
a)In Preorder traversal
It traverse the root first then left subtrees and finally right sub trees.

Preorder traversal for T
It first visits root node A then to left root B
Then to the child left E and right F
Root node has sub tree C and D as well so it visits C first which is left among C and D
Then, it visits D which has one child G which doesnt have any children
Therefore preorder traversal of T is "A, B, E, F, C, D, G"

Preorder traversal for T'
First it visit the root node A then to left node B then to child node E
The node E has a right child so it visits F
Since, B has a right subtree then it visits to C which also has D
Finally D has a left child G
Therefore preorder traversal of T' is "A, B, E, F, C, D, G"

Therefore preorder traversal T and T' are equivalent

b)In Postorder traversal
It taverses the left subtree first then to the right sub trees and finally to root node

Postorder traversal of T
It first visits the left most node E followed with the right node F which has root node B
After it visits to B then it visits to C followed up by G and the root node
Then finally the root node of the tree A
Therefore the post order traversal of T is "E, F, B, C, G, D, A"

Postorder traversal of T'
It first visits the left most child node but the left node in tree doesnt consist of left child node so it visits right child
It visits F first followed by E then to the left node of D which is G followed by D
Then it visits the root of D which is C then root of C which is B then the main root A
Therefore the post order traversal of T' is "F, E, G, D, C, B, A"

Therefore postorder traversal of T and T' are not equivalent

c)In inorder tranversal
It tranverses left subtrees first then the root and the right most sub tree

Inorder tranversal of T'
In this case it first visits the root node E as it doesnt have left child node followed with the right child F
Then, it visits the root node of E which is B then right sub tree C
Then, it visits the left child node of D and D as it is root of G and finally A which is the main root of all.

Therefore the inorder tranversal of T' is "E, F, B, C, G, D, A"

Therefore the inorder tranversal of T' is equivalent to the postorder tranversal of T.
'''