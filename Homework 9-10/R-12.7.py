def union(A, B):
    S = []
    S += A
    for i in B:
        if i not in S:
            S.append(i)

    return sorted(S)

A = [1,2,3]
B = [3,5,4]
print(union(A, B))

'''
From the above code we can assume A and B as a sequence 
and union as a function
A and B are processed where S is empty initially 
Add all the element of A into S so that we get element of A in new list
check if each element of B as if it matches to new S
If it doesnot matches then add it to the S sequence
finally sort it
Then we get our AUB with no duplicate as a sorted sequence.
'''