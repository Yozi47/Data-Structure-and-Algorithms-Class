'''
A is a collection of n elements
Let us take B is an empty list
loop the elements of A and check if the element is already present in B or not
If B consist of the element on that loop of A then skip the element
Else add the element in B
'''

A = [1,2,3,4,4,4]
B = []
for i in A:
    if i not in B:
        B.append(i)
print(B)

'''The output for A will be B which is 1,2,3,4'''
