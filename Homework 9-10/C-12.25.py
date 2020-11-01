'''
a) To check if T is sorted or not
loop the sequence to the end
check the previous element is less or not
check the next element
Return the result as sorted if each previous element is less
else return as unsorted
The time complexity for algorithm is O(n)

b) In the condition, we are given that T is sorted but we are
unsure if it is true or not
To figure out if the elements in T are sorted or not, all the
elements in S should be scanned to every element in T
As the sequence S and T consists of elements repeating and contains
duplicate elements, the algorithm isSorted is not sufficient.
The running time complexity for this is O(n*n)

c) For this the Linda's algorithm should check for the sorted
elements are in increasing order or not
Then all elements should be scanned only once which has time
complexity of O(n)
'''