# C-4.12
def product(m, n):
    if m == 1:
        return n
    elif n == 1:
        return m
    elif m == 0 or n == 0:
        return 0
    else:
        return m + product(m, n-1)

m = int(input("Enter 1st number: "))
n = int(input("Enter 2nd number: "))
print("The product of two number: ", product(m, n))

'''
"Algorithm"
Check m and n if they are 1 or not
If m is 1 then return the value n or if n is 1 then return the value m
If any one of them are 0 return the value 0
If non of condition above works then call the product() function with m and n-1
Call the product function until and unless above condition n equals 1 is obtained
then return the obtained product
'''
