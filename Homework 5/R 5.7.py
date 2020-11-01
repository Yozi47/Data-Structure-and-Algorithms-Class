A = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]  # considering A as an array of size n >= 2 containing integer from 1 to n-1
get_num = 0
for i in range(len(A)):  # looping the number of elements
    check = 0
    for j in range(len(A)):  # looping the number of elements
        if A[i] == A[j]:  # checking for common number
            check += 1
    if check >= 2:  # if 2 common number are found then add that number to get_num
        get_num = A[i]
print("The repeated number is: ", get_num)

'''
From the above code and question, A is an array with size n>=2 containing integer from 1 to n-1
with exactly one repeated.
In above code, a loop inside a loop is used in which first loop iterate n times
and same with the second loop
Then each element in the array is checked if there is common number or not
In 1 complete iteration there would be 1 common number except for that number which is repeated
It the iteration gives 2 common number which means the obtained number is repeated
Then the result is the obtained number
'''
