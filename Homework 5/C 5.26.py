B = [1, 2, 3, 3, 3, 3, 3, 4, 5]  # considering B as an array of size n >= 6 containing integer from 1 to n-5
get_num = 0
for i in range(len(B)):  # looping the number of elements
    check = 0
    for j in range(len(B)):  # looping the number of elements
        if B[i] == B[j]:  # checking for common number
            check += 1
    if check >= 5:  # if 5 common number are found then add that number to get_num
        get_num = B[i]
print("The repeated number is: ", get_num)

'''
From the above code and question, B is an array with size n >= 6 containing integer from 1 to n-5
with exactly five repeated.
In above code, a loop inside a loop is used in which first loop iterate n times
and same with the second loop
Then each element in the array is checked if there is common number or not
In 1 complete iteration there would be 1 common number except for that number which is repeated number.
The repeated number iteration gives 5 common number which means the obtained number is repeated number
Then, the result is the obtained number
'''
