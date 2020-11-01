# R 5.12

list = [[1, 2], [2, 3], [3, 4], [4, 5]]  # Let us consider list of list
sums = 0  # final sum to be calculated
for i in list:  # loop the list beginning with [1,2]
    sums += sum(i)  # operator sum to calculate the sum inside a list eg[1,2] = 3
print(sums)

'''
From the above code we get a list of list
sums is the initiation for the final sum of the given number
iterate the number of list inside the list and add each number in list and add to the sums
then the final result is obtained.
'''