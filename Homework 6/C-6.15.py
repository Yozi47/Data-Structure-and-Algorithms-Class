def compar(S):  # defining a function with Stack S as parameter
    x = S.pop()  # popping up last element of Stack S
    return max(S.pop(), x)  # returning compared maximum element

'''
From above code
Considering Stack S is [X,Y,Z]
The variable x is Z.
The returned item is max between Z and Y which means one number is eliminated
    between two of the number Z or Y.
That means the remaining either X and Z or X and Y have two possibilities of getting
    the right largest number.
So, we get the probability of 2/3.
'''