# R-4.1
def maximum(sequence, n):
    if n == 1:  # checking if the sequence has 1 element and return the element
        return sequence[0]
    else:  # compare the sequence elements by calling maximum function recursively to find
            # and return the maximum sequence element
        return max(maximum(sequence, n-1), sequence[n-1])
list = [1, 2, 35, 15, 5]
print(maximum(list, len(list)))
'''
"Description"
The running time of above code can be obtain by the following
There is the comparision of sequence elements to find maximum element in the sequence recursively
if there is only one element there is no comparision and returns the element given
the compare sequence value until n-1 by the maximum() function
the sequence value is a[n] is n which means the recursion will carryout for n times for n items
in a sequence.
So, the usage space and running time for the n number of sequence is O(n)
 '''