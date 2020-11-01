'''
Codes from D2l
Answer Codes are written below after the sorting methods functions
'''
def merge(S1, S2, S):
    """Given sorted lists S1 and S2, merge them into a new sorted list."""
    i = j = 0

    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    # DIVIDE
    mid = n//2
    S1 = S[:mid]
    S2 = S[mid:]

    # CONQUER
    merge_sort(S1)
    merge_sort(S2)

    # COMBINE
    merge(S1, S2, S)

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def bubble_sort(L):
    """In place sorting of a list L."""
    # we must assume the worst case scenario
    for i in range(len(L) - 1):    # number of possible swaps per pass
        # iterate over all pairs until just before the last unsorted element
        for j in range(len(L) - i - 1):
            # compare consecutive pairs; swap if not in order
            if L[j] > L[j + 1]:
                swap(L, j, j+1)


def quick_sort(L):
    """Return a sorted version of list L."""
    n = len(L)
    if n < 2:
        return

    # DIVIDE
    p = L[-1]       # last element as pivot p
    left = []       # holds elements < p
    right = []      # holds elements > p
    equal = []      # holds elements = p
    i = 0           # index to traverse the list

    while L != []:
        if L[i] < p:
            left.append(L.pop(i))
        elif L[i] > p:
            right.append(L.pop(i))
        else:
            equal.append(L.pop(i))

    # CONQUER
    quick_sort(left)
    quick_sort(right)

    # COMBINE
    while left != []:
        L.append(left.pop(i))
    while equal != []:
        L.append(equal.pop(i))
    while right != []:
        L.append(right.pop(i))


'''Exam Code starts from Here'''

if __name__ == '__main__':
    import random
    import time
    # creating a random number of lists
    no_of_list = random.randrange(5, 10)
    list = []  # main list
    for i in range(no_of_list):
        list_dup = [] # sub list
        for j in range(random.randrange(50, 1000)):
            # adding data into a sub list
            list_dup.append(random.randrange(1, 100))
        list.append(list_dup)

    # Testing portion
    time_bubble = []
    time_merge = []
    time_quick = []

    for sub_list in list:
        # Gathering the time required for bubble sort
        x = time.time()
        bubble_sort(sub_list)
        y= time.time()
        time_ = y - x
        time_bubble.append(time_)

        # Gathering the time required for merge sort
        start = time.time()
        merge_sort(sub_list)
        end = time.time()
        time_ = end - start
        time_merge.append(time_)

        # Gathering the time required for quick sort
        start_quick = time.time()
        quick_sort(sub_list)
        end_quick = time.time()
        time_ = end_quick - start_quick
        time_quick.append(time_)


    # Plotting the obtain time from different sorting methord
    from pylab import *
    plot(arange(0, len(time_bubble)),time_bubble,'.-',label="Bubble")
    plot(arange(0, len(time_merge)), time_merge, '.-', label="Merge")
    plot(arange(0, len(time_quick)), time_quick, '.-', label="Quick")
    xlabel('Number of attempt to sort the list')
    ylabel('Time taken to sort the list')
    title('JPT')
    legend(('Bubble','Merge', 'Quick'))
    show()

