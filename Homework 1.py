# Question no 1 (R-1.4)
def sum_sqr():
    sum = 0
    n = int(input("Enter a number"))
    for i in range(1,n+1):  # Looping from 1 to the number n term.
        sum += i*i  # multiplying the number by itself (squaring) and adding as some.
    print("The sum is ",sum)
sum_sqr()
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#Question no 2 (R-1.11)
list = []
for i in range(9):
    list.append(2**i)  # getting the increasing power value of 2
print(list)
print()


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#Question no 3 (R-1.12)
import random
def my_choice(word):
    x = word[random.randrange(len(word))]   # Using randrange to get random position
    return x
word = "Rocket"  # Assuming input as word Rocket
print("A random choice element from given is :",my_choice(word))
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 4 (C-1.14)
list = [1,2,6,8]
x = 0
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if (list[i] * list[j]) % 2 == 1:  # checks if the product of two number is odd
            x = 1
if x == 1:
    print("It has distinct pair of number whose product is odd")
else:
    print("It does not consist of distinct pair having product odd")
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 5 (C-1.19)
import string
list=[]
for i in string.ascii_lowercase:
    list.append(i)  # insert the alphabets in the list.
print(list)

print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 6 (C-1.21)
lines = []
while True:
    try:
        print("Type the sentence and press enter or Ctrl + D to end")
        line = input()
        lines.append(line)  # Insert sentence in a list
    except EOFError:  # Checks for end of file
        break  # End the loop
x = reversed(lines)  # reverse the order
for i in x:
    print(i)
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 7 (C-1.22)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []
for k in range(len(a)):
    c.append(a[k]*b[k])  # Get the product of a and b and add it to list c
print(c)
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 8 (C-1.23)
list = [1, 2, 3, 4, 5, 6, 7]
try:
    list[7] = 7
except IndexError:
    print("Don't try buffer overflow attacks in Python!")
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 9 (C-1.27)
def fact(n):
    list = []
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            list.append(n//k)
        k += 1
    if k * k == n:
        yield k
    for value in reversed(list):
        yield value
for i in fact(100):
    print(i, end=" ")
print()
print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 10 (C-1.28)
import math
def norm(v, p=2): # Defining a function
    sum = 0
    for value in v:
        sum += (value**p)  # add the power value of p
    length = math.sqrt(sum)  # Taking a square root
    return length
print(norm([4, 3]))  # Call and print the statement
print()
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Question no 11 (C-1.36)
read = "This is the random text trying to get the output of the code"
lol = read.split()  # Spliting the sentence
dict = {}
for i in lol:  # looping the distinct words
    count = 0
    for j in lol:
        if i == j:  # checking the repeated word
            count += 1
    dict1 = {i: count}
    dict.update(dict1)  # Updating the dictionary
    count = 0
print(dict)
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
