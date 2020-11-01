
"""R-3.6 What is the sum of all the even numbers from 0 to 2n, for any positive integer n?"""

n = int(input("Enter a number: "))
sum = 0
last_no = 2 * n
for i in range(0, last_no+1, +2):
    sum += i
print("The sum of all even number from 0 to 2n is: ", sum)
